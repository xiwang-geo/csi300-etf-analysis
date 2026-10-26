FINANCIAL PRODUCT ANALYTICS

# Same index. More than returns.

Compare fees, trading activity and tracking across five CSI 300 ETFs. Turn the evidence into an interactive screening and comparison tool.

[Explore the tool **↗**](../app/comparison-tool.html) · [Read the report **↗**](report.pdf)

COMPLETED STUDY · DATA THROUGH 2026-10-23

THE RESEARCH QUESTION

## Same fees. Same product experience?

**0.20% / year**

Verified management + custody fees for all five funds

Largest / smallest median daily turnover: **231×**

Equal fees do not remove differences in activity, observation windows or measurement.

**Scope:** 5 ETFs · 3 windows · 242 main-window daily returns · 15 fund-window comparisons · 2 implemented priority features.

01 / COMPARABLE EVIDENCE

## A different window. A different tracking-error leader.

Five funds and one common end date. Three prespecified observation windows.

### Annualized ex-post tracking error

Against H00300 total return · Lower means less variation in daily return differences

| ETF | 12 months | 6 months | 3 months |
| --- | ---: | ---: | ---: |
| 510300 | 0.194% | 0.261% | 0.140% |
| 510310 | 0.162% | 0.223% | 0.181% |
| 510320 | 0.336% | 0.393% | 0.311% |
| 510330 | 0.161% | 0.224% | 0.156% |
| 510350 | 0.510% | 0.641% | 0.823% |

[Source CSV](../data/收益风险与跟踪指标_三窗口.csv)

A / WINDOW EFFECT

### 12-month lowest observation: 510330

Only about 0.001144 percentage points below 510310. A tiny historical difference is not a stable advantage.

#### Product response

Synchronize every table, chart, date and denominator when the window changes. Compare individual metrics without an arbitrary “best ETF” composite score.

INFORMATION DESIGN

Sample standard deviation × √252 against the same total-return reference. This is not a contractual compliance assessment. Windows overlap; their rankings are not independent evidence or forecasts.

02 / WHAT CHANGES THE INTERPRETATION

## Before comparing numbers, check what makes them comparable.

B / TYPICAL VS. AVERAGE

**231×**

### A wide activity gap

Main-window median daily turnover differs by about 231×. In high-turnover-day removal scenarios, means fall about 4.71%–27.50%; medians change less.

Turnover describes historical activity. It does not measure spreads, depth or actual execution cost.

C / DISTRIBUTIONS MATTER

**2 → 4**

### Definitions change the order

Ignoring distributions and substituting raw unit-NAV change for total return moves 510310 from observed rank 2 to an erroneous rank 4 in the main window.

The incorrect definition is diagnostic only. Accepted total return assumes theoretical reinvestment on the ex-dividend date.

D / PRECISION LIMITS

**9 / 30**

### Some differences cannot be separated

Across three windows, 9 of 30 pairwise comparisons of absolute closing-premium P95 overlap under the prespecified quote-rounding scenario.

Conditional precision bounds are not confidence intervals or executable arbitrage returns.

03 / FROM ANALYSIS TO PRODUCT

## Make the comparison easier to understand.

[Explore the prototype ↗](../app/comparison-tool.html)
![Original Chinese-language comparison tool with window filters, product selection and metric explanations](../assets/tool-preview.png)

F1

### One window, side-by-side comparison

Filter on separate metrics and compare 2–3 funds. Switching 12-, 6- and 3-month windows synchronizes tables, chart bases and dates.

F2

### Definitions and sources within reach

Place return definitions, fee components, missing-data states, precision and snapshot dates beside the comparison.

**Implementation**

The prototype passed 24 development function checks and two source-menu checks. **Real participants: 0. User effects remain untested.** Development events do not establish accuracy, completion-time or conversion improvements. The original tool and full report are in Chinese; this case and the executive summary provide English coverage.

04 / HOW THE EVIDENCE WAS BUILT

## Each comparison has a check behind it.

Source responses become an aligned fund-day panel, then window comparisons and product features. The scope is five selected Shanghai-listed, CNY-denominated funds: 510300, 510310, 510320, 510330 and 510350.

- 01

### Sources and alignment

1,215 price rows, 1,215 NAV rows and 486 index rows; three distributions and ten fee intervals. Effective dates and observation dates remain distinct.

- 02

### Processing and reconciliation

242, 121 and 60 daily returns, each with its own preceding seed date. Results were reconstructed from source responses and notices; the repository also independently checks 120 metric values from the included source snapshot.

- 03

### Robustness and limits

Check windows, high-turnover dates, distribution definitions and quote precision. Missing historical shares, order books and real-user logs limit the conclusions.

05 / READ · EXPLORE · REPRODUCE

## Follow a finding back to its evidence.

DATA CUTOFF / 2026.10.23[01 / REPORT**Full report**9-page PDF · Chinese**↗**](report.pdf) · [02 / ENGLISH**Executive summary**Scope, findings and limitations**↗**](english-summary.md)[03 / PRODUCT**Comparison tool**Offline prototype · Chinese**↗**](../app/comparison-tool.html) · [04 / REPRODUCE**GitHub repository**SQL · CSV · SQLite · Python**↗**](https://github.com/xiwang-geo/csi300-etf-analysis)

ANOTHER PERSPECTIVE

## From financial products to onchain activity.

A second case: activity composition, address return and concentration in one Uniswap pool.

[Read the onchain case ↗](https://github.com/xiwang-geo/uniswap-base-analysis)
