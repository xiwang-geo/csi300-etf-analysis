# CSI 300 ETF Comparison and Fund Screening Tool Design

## Executive summary

Five Shanghai-listed, CNY-denominated CSI 300 ETFs were compared using public price, net asset value (NAV), dividend and index data. The main observation window is 24 October 2025 to 23 October 2026, with 242 daily returns and a baseline on 23 October 2025. Prespecified six- and three-month windows contain 121 and 60 daily returns. The sample does not represent the entire ETF market.

Main-window theoretical NAV total returns range from -8.965% to -7.720%, while annualized daily volatility ranges from approximately 17.45% to 17.77%. All five have verified annual management and custody fee rates of 0.15% and 0.05%, respectively. Nevertheless, the highest and lowest median daily trading values differ by approximately 231 times. Fee equality therefore does not make the products interchangeable, or imply identical total execution costs.

## Method and findings

Fund returns incorporate verified cash distributions, assuming theoretical reinvestment at NAV on the ex-dividend date. Payment delays and reinvestment transaction costs are not modeled. The primary research reference is the H00300 gross total return index; 000300 is retained separately as a price-index comparison. Annualized ex-post tracking error uses a sample standard deviation and a factor of 252. These research measures are not assessments of compliance with contractual tracking targets.

The ETF with the lowest observed tracking error changes across the three windows. The top three products by median daily trading value remain the same, while the two smaller products can exchange positions. Removing a common union of high-trading-value dates changes the levels but not the within-window mean or median trading-value order. Main estimates retain all original observations.

A conditional quote-rounding analysis cannot reliably separate the main-window absolute closing premium P95 of 510300 and 510310. These conservative rounding bounds are not confidence intervals. The largest absolute closing deviation is a verified 0.9822% premium for 510320 on 17 July 2026. It is a daily closing-price/NAV observation, not evidence of an executable intraday arbitrage opportunity.

## Product output and limitations

Two functions were implemented in an offline comparison prototype: consistent-window filtering and side-by-side comparison of two or three ETFs; contextual metric definitions, precision limitations and provenance. Baseline and revised interfaces share identical data and task answers. The prototype passed 24 development functional checks plus two source-menu checks. Three scored tasks, an event dictionary and a future validation plan are included.

There are no real participant results or measured conversion improvements. Historical share counts, net flows, bid-ask spreads, market depth and NAV publication timestamps are unavailable. Five correlated funds and overlapping windows do not establish independent statistical evidence or predict future returns. Raw records and issuer dividend notices were independently reprocessed to reconstruct the complete main-window result table; values agree within the frozen calculation tolerances.
