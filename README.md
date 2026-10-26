# CSI 300 ETFs — Comparable Evidence & Product Design

**English** · [简体中文](README.zh-CN.md)


![Research cover](assets/cover.svg)

Compare **five same-index ETFs** across fees, risk, tracking and trading activity, then turn the evidence into an interactive fund-comparison tool.

[Case study](reports/case-study.en.md) · [9-page report](reports/report.pdf) · [English summary](reports/english-summary.md) · [Offline comparison tool](app/comparison-tool.html)

> Download the HTML tool and open it in a browser. GitHub file preview displays source rather than executing the application.

## What the analysis established

- Known management + custody fees are **0.20% per year** for all five candidates, yet largest/smallest median daily turnover differs by approximately **231×** in the main window.
- The lowest observed tracking-error fund changes across the predefined **12-, 6- and 3-month windows**. Window and return definitions belong in the comparison interface.
- Ignoring distributions moves 510310 from observed return rank **2 to 4** in the main window. The erroneous definition is a diagnostic comparison, not an accepted return measure.
- In a disclosed quote-rounding scenario, **9 of 30** pairwise absolute closing-premium P95 comparisons cannot be separated. Those bounds are not confidence intervals.

## Scope and sources

Candidates: **510300, 510310, 510320, 510330, 510350**, all Shanghai-listed RMB CSI 300 ETFs. Main window: **2025-10-24 to 2026-10-23**, with seed 2025-10-23. Window daily-return counts: **242 / 121 / 60**. This is a selected candidate set, not the whole market.

Sources include SSE daily quotes, 65 Eastmoney NAV pages, CSI price/total-return series and reviewed issuer notices. Quote and NAV inputs each have **1,215 rows**, benchmark inputs **486 rows**; three distributions and ten fee intervals are retained. **H00300 total return** is the research reference; contract-compliance evaluation is not performed.

## Implemented product

1. Same-window filters and comparison of **2–3 funds**; tables, dates and chart bases move together.
2. Nearby metric explanations, precision and source notes, missing-data and snapshot-date states.

The tool passed **24 development function checks plus two source-menu checks**. Real participants: **0**. No user conversion, task-accuracy uplift or completion-time improvement has been established. The prototype includes a measurement design, not an executed user experiment.

## Reproduce

Python 3.10+; standard library only. No account, API key or live market access.

```bash
python scripts/reproduce.py
```

The script recalculates **eight metrics × fifteen product-windows** from the included source-fact snapshot: total return, volatility, maximum drawdown, total-return tracking error, mean/median/P10 turnover and absolute closing-premium P95. It reconciles against the published CSVs without changing the database. Full raw-response re-extraction is outside this curated repository.

## Repository map

| Path | Contents |
| --- | --- |
| `reports/` | Chinese full report and English summary |
| `app/` | Portable interactive tool |
| `sql/` | Model, joins, checks, wealth and tracking queries |
| `data/` | Source SQLite snapshot, inputs, results and robustness tables |
| `scripts/reproduce.py` | Independent source-fact recalculation |
| `SOURCE-NOTES.md` | Scope and database checksum |

## Limits

Historical comparisons do not predict future returns. Turnover is not spread or execution cost. Closing premium is not an executable intraday arbitrage return. Historical shares, order books and real-user logs are unavailable. Known ongoing fees are already reflected in NAV and are not deducted a second time.
