"""Recompute eight metrics for five ETFs in three frozen windows.
Uses source fact tables in the supplied read-only snapshot, not stored metric values.
Standard library only, Python 3.10+. No external APIs or filesystem writes.
"""
from pathlib import Path
from decimal import Decimal
import csv,json,hashlib,sqlite3,statistics,math

ROOT=Path(__file__).resolve().parents[1]
def read_csv(name):
    with (ROOT/'data'/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def quantile(values,q):
    a=sorted(values);z=(len(a)-1)*q;i=int(z);return a[i]+(a[min(i+1,len(a)-1)]-a[i])*(z-i)
def main():
    path=ROOT/'data/source.sqlite';before=hashlib.sha256(path.read_bytes()).hexdigest()
    con=sqlite3.connect(path.as_uri()+'?mode=ro',uri=True);con.row_factory=sqlite3.Row
    expected=read_csv('收益风险与跟踪指标_三窗口.csv')
    trading={(r['window_id'],r['product_id']):r for r in read_csv('交易活跃度与收盘折溢价_三窗口.csv')}
    benchmark={r['trade_date']:Decimal(r['point_close_decimal']) for r in con.execute("select * from fact_benchmark_daily where series_id='H00300'")}
    checked=[]
    for row in expected:
        pid=row['product_id'];start=row['start_date'];end=row['end_date'];seed=row['seed_date']
        nav={r['nav_date']:Decimal(r['unit_nav_decimal']) for r in con.execute('select * from fact_nav_daily where product_id=?',(pid,))}
        actions=list(con.execute('select * from fact_corporate_action where product_id=?',(pid,)))
        cash={}
        for action in actions:
            if seed<action['effective_date']<=end:
                assert Decimal(action['share_factor_decimal'])==1,'A split requires an explicit unit adjustment.'
                cash[action['effective_date']]=cash.get(action['effective_date'],Decimal(0))+Decimal(action['cash_per_unit_decimal'] or '0')
        prices=list(con.execute('select * from fact_price_daily where product_id=? and trade_date between ? and ? order by trade_date',(pid,start,end)))
        assert len(prices)==int(row['valid_n'])==int(row['expected_n'])
        previous=seed;returns=[];active=[];turnover=[];premiums=[];wealth=1.0;peak=1.0;drawdowns=[]
        for p in prices:
            day=p['trade_date'];rf=float((nav[day]+cash.get(day,Decimal(0)))/nav[previous]-1)
            rb=float(benchmark[day]/benchmark[previous]-1)
            returns.append(rf);active.append(rf-rb);turnover.append(float(p['turnover_cny_decimal']))
            premiums.append(abs(float(Decimal(p['close_decimal'])/nav[day]-1)))
            wealth*=1+rf;peak=max(peak,wealth);drawdowns.append(wealth/peak-1);previous=day
        results={'total_return':wealth-1,'annualized_volatility':statistics.stdev(returns)*math.sqrt(252),'max_drawdown':min(drawdowns),'tracking_error_TR':statistics.stdev(active)*math.sqrt(252),'turnover_mean_cny':statistics.mean(turnover),'turnover_median_cny':statistics.median(turnover),'turnover_p10_cny':quantile(turnover,.1),'abs_premium_p95':quantile(premiums,.95)}
        key=(row['window_id'],pid)
        for metric,value in results.items():
            target=float(row[metric] if metric in row else trading[key][metric]);tol=1e-6 if metric.startswith('turnover_') else 1e-10
            assert abs(value-target)<=tol,(key,metric,value,target)
        checked.append({'product_id':pid,'window_id':row['window_id'],'daily_returns':len(prices),'metrics_checked':len(results)})
    counts={name:con.execute('select count(*) from '+name).fetchone()[0] for name in ['fact_price_daily','fact_nav_daily','fact_benchmark_daily','fact_corporate_action','dim_fee_interval']}
    assert counts['fact_price_daily']==counts['fact_nav_daily']==1215 and counts['fact_benchmark_daily']==486
    assert len(checked)==15 and hashlib.sha256(path.read_bytes()).hexdigest()==before
    con.close()
    print(json.dumps({'passed':True,'network_calls':0,'source_snapshot_unchanged':True,'source_fact_counts':counts,'product_windows':len(checked),'metric_values_checked':sum(x['metrics_checked'] for x in checked),'results':checked},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
