# Just another market stock value scoring algorithm

There are as many strategies for selecting stocks for an investment portfolio as there are personalities in the world. The present algorithm based on **yfinance `0.1.62`** and **pytickersymbols `1.4.3`** is only intended to share a basic example using publicly available business information.

## Investment disclaimer

This project is distributed for general informational and educational purposes only and is not intended to constitute investment advice.

## Glosary

**PriceToEarningsRatio:** The price-to-earnings ratio (P/E ratio) is the ratio for valuing a company that measures its current share price relative to its per-share earnings (EPS). The price-to-earnings ratio is also sometimes known as the price multiple or the earnings multiple. [Learn more][1]

**PriceToSalesRatio:** The price-to-sales ratio (Price/Sales or P/S) is calculated by taking a company's market capitalization (the number of outstanding shares multiplied by the share price) and divide it by the company's total sales or revenue over the past 12 months. The lower the P/S ratio, the more attractive the investment. [Learn more][2]

**EV_EBITDA:** The enterprise value (EV) to the earnings before interest, taxes, depreciation, and amortization (EBITDA) ratio varies by industry. EBITDA measures a firm's overall financial performance, while EV determines the firm's total value. [Learn more][3]

**EV_R:** The enterprise value-to-revenue (EV/R) multiple helps compare a company’s revenues to its enterprise value. The lower the better, in that, a lower EV/R multiple signals a company is undervalued. The EV/R multiple is also often used to determine a company's valuation in the case of a potential acquisition. It's also called the enterprise value-to-sales multiple. [Learn more][4]

## Results

| Company                         | Symbol   | Yahoo Symbol   |       P/E |    P/E PC |       P/S |   P/S PC |   EV/EBITDA |   EV/EBITDA PC |   EV/R |   EV/R PC |   Score |
|:--------------------------------|:---------|:---------------|----------:|----------:|----------:|---------:|------------:|---------------:|-------:|----------:|--------:|
| Costco Wholesale Corporation    | COST     | COST           |  42.1689  |  73.4043  |  0.977768 | 84.0426  |      20.052 |       63.8298  |  0.932 |  93.617   | 78.7234 |
| Wm Morrison Supermarkets PLC    | MRW      | MRW.L          |  66.225   |  90.4255  |  0.362737 | 96.8085  |      11.203 |       22.3404  |  0.499 |  98.4043  | 76.9947 |
| adidas AG                       | ADS      | ADS.F          |  64.4007  |  88.2979  |  2.98367  | 48.9362  |      31.882 |       81.9149  |  3.048 |  60.6383  | 69.9468 |
| JD Sports Fashion plc           | JD       | JD.L           |  41.6087  |  71.2766  |  1.60081  | 70.2128  |      16.822 |       56.383   |  1.709 |  76.5957  | 68.617  |
| United Parcel Service Inc.      | UPS      | UPS            |  36.1229  |  64.8936  |  2.09477  | 62.766   |      21.231 |       70.2128  |  2.194 |  71.2766  | 67.2872 |
| Johnson Matthey PLC             | JMAT     | JMAT.L         |  29.718   |  47.8723  |  0.390449 | 95.7447  |      10.171 |       18.0851  |  0.431 | 100       | 65.4255 |
| Ford Motor Company              | F        | F              |  14.5674  |  11.7021  |  0.447873 | 93.617   |      21.708 |       71.2766  |  1.422 |  82.9787  | 64.8936 |
| Amazon.com Inc.                 | AMZN     | AMZN           |  70.761   |  92.5532  |  4.47535  | 38.2979  |      32.918 |       84.0426  |  4.49  |  43.617   | 64.6277 |
| Ferguson PLC                    | FERG     | FERG.L         |  34.1471  |  57.4468  |  1.04231  | 80.8511  |      11.846 |       29.7872  |  1.018 |  90.4255  | 64.6277 |
| Vodafone Group PLC              | VOD      | VOD            | 333.4     |  97.8723  |  1.06052  | 79.7872  |       9.491 |       11.7021  |  2.613 |  63.8298  | 63.2979 |
| Walmart Inc.                    | WMT      | WMT.F          |  30.1371  |  51.0638  |  0.588718 | 89.3617  |       9.51  |       13.2979  |  0.67  |  95.7447  | 62.367  |
| NIKE Inc.                       | NKE      | NKE.F          |  75.4353  |  93.617   |  5.54695  | 28.7234  |      34.012 |       85.1064  |  4.583 |  41.4894  | 62.234  |
| CRH PLC                         | CRH      | CRH            |  35.5712  |  63.8298  |  1.4307   | 73.4043  |      11.879 |       30.8511  |  1.688 |  77.6596  | 61.4362 |
| Starbucks Corporation           | SBUX     | SBUX           | 138.363   |  96.8085  |  5.80534  | 27.6596  |      44.572 |       91.4894  |  6.346 |  28.7234  | 61.1702 |
| NEXT PLC                        | NXT      | NXT.L          |  35.3312  |  61.7021  |  2.94907  | 51.0638  |      26.478 |       78.7234  |  3.503 |  51.0638  | 60.6383 |
| Rentokil Initial PLC            | RTO      | RTO.F          |  49.9145  |  76.5957  |  4.06042  | 41.4894  |      21.159 |       69.1489  |  3.939 |  47.8723  | 58.7766 |
| DS Smith PLC                    | SMDS     | SMDS.L         |  30.2979  |  52.1277  |  0.981738 | 82.9787  |       9.51  |       13.2979  |  1.278 |  85.1064  | 58.3777 |
| Ashtead Group PLC               | AHT      | AHT.F          |  37.9947  |  69.1489  |  1.90604  | 63.8298  |      12.044 |       31.9149  |  2.5   |  67.0213  | 57.9787 |
| Bunzl PLC                       | BNZL     | BNZL.L         |  19.9221  |  21.2766  |  0.852491 | 85.1064  |      12.06  |       32.9787  |  0.96  |  92.5532  | 57.9787 |
| Caterpillar Inc.                | CAT      | CAT            |  34.7649  |  60.6383  |  2.76976  | 56.383   |      18.818 |       60.6383  |  3.417 |  54.2553  | 57.9787 |
| Bayerische Motoren Werke AG     | BMW      | BMW.F          |  15.3246  |  13.8298  |  0.558448 | 90.4255  |      14.33  |       44.6809  |  1.464 |  80.8511  | 57.4468 |
| Exelon Corporation              | EXC      | EXC            |  40.4595  |  70.2128  |  1.28386  | 75.5319  |       9.937 |       17.0213  |  2.504 |  65.9574  | 57.1809 |
| Accenture PLC                   | ACN      | ACN            |  36.9965  |  67.0213  |  4.35047  | 39.3617  |      23.745 |       75.5319  |  3.945 |  46.8085  | 57.1809 |
| Smiths Group PLC                | SMIN     | SMIN.L         |  25.9776  |  40.4255  |  2.61398  | 57.4468  |      21.118 |       68.0851  |  3.041 |  61.7021  | 56.9149 |
| Koninklijke Ahold Delhaize N.V. | AD       | AD.AS          |  20.6016  |  27.6596  |  0.347832 | 97.8723  |       7.592 |        4.25532 |  0.509 |  96.8085  | 56.6489 |
| FedEx Corporation               | FDX      | FDX.F          |  26.2323  |  41.4894  |  0.792023 | 86.1702  |       8.257 |        6.38298 |  1.156 |  89.3617  | 55.8511 |
| Pearson PLC                     | PSON     | PSON.L         |  20.0341  |  22.3404  |  1.82859  | 65.9574  |      18.793 |       59.5745  |  2.019 |  73.4043  | 55.3191 |
| AVEVA Group plc                 | AVV      | AVV.L          | 347.257   |  98.9362  | 14.4051   | 10.6383  |      74.339 |       97.8723  | 14.09  |  11.7021  | 54.7872 |
| Daimler AG                      | DAI      | DAI.F          |   9.9959  |   6.38298 |  0.495801 | 92.5532  |      12.299 |       35.1064  |  1.283 |  84.0426  | 54.5213 |
| Dow Inc.                        | DOW      | DOW            |  23.8308  |  38.2979  |  1.15905  | 78.7234  |      10.944 |       21.2766  |  1.535 |  79.7872  | 54.5213 |
| Target Corporation              | TGT      | TGT            |  20.2956  |  25.5319  |  1.25305  | 76.5957  |      11.538 |       27.6596  |  1.272 |  86.1702  | 53.9894 |
| Intertek Group PLC              | ITRK     | ITRK.L         |  36.7585  |  65.9574  |  3.29767  | 46.8085  |      16.506 |       53.1915  |  3.516 |  50       | 53.9894 |
| Tesla Inc.                      | TSLA     | TSLA           | 658.267   | 100       | 17.6088   |  7.44681 |     138.28  |       98.9362  | 17.51  |   8.51064 | 53.7234 |
| Deutsche Post AG                | DPW      | DPW.F          |  19.126   |  18.0851  |  1.02736  | 81.9149  |      11.488 |       26.5957  |  1.203 |  87.234   | 53.4574 |
| Netflix Inc.                    | NFLX     | NFLX           |  64.8651  |  89.3617  |  9.00494  | 15.9574  |      42.652 |       89.3617  |  9.228 |  19.1489  | 53.4574 |
| Booking Holdings Inc.           | BKNG     | BKNG           | 128.354   |  95.7447  | 15.9516   |  8.51064 |     172.747 |      100       | 16.85  |   9.57447 | 53.4574 |
| Spirax-Sarco Engineering PLC    | SPX      | SPX.L          |  59.6678  |  87.234   |  8.65981  | 18.0851  |      34.705 |       86.1702  |  8.5   |  20.2128  | 52.9255 |
| Siemens AG                      | SIE      | SIE.F          |  18.1338  |  17.0213  |  1.81355  | 67.0213  |      16.873 |       57.4468  |  2.242 |  70.2128  | 52.9255 |
| Tesco PLC                       | TSCO     | TSCO.L         |   2.94913 |   3.19149 |  0.317485 | 98.9362  |       9.334 |       10.6383  |  0.499 |  98.4043  | 52.7926 |
| salesforce.com Inc.             | CRM      | CRM            |  55.9498  |  82.9787  | 10.112    | 14.8936  |      61.911 |       94.6809  |  9.629 |  18.0851  | 52.6596 |
| PayPal Holdings Inc.            | PYPL     | PYPL           |  68.4161  |  91.4894  | 15.4211   |  9.57447 |      67.031 |       95.7447  | 14.582 |  10.6383  | 51.8617 |
| Lowe's Companies Inc.           | LOW      | LOW            |  21.3056  |  30.8511  |  1.46355  | 71.2766  |      11.418 |       25.5319  |  1.671 |  78.7234  | 51.5957 |
| General Dynamics Corporation    | GD       | GD             |  17.2927  |  15.9574  |  1.41199  | 74.4681  |      12.962 |       40.4255  |  1.719 |  75.5319  | 51.5957 |
| The Home Depot Inc.             | HD       | HD             |  23.4794  |  35.1064  |  2.42282  | 59.5745  |      14.774 |       46.8085  |  2.609 |  64.8936  | 51.5957 |
| Halma PLC                       | HLMA     | HLMA.L         |  51.7724  |  78.7234  |  7.99207  | 22.3404  |      32.148 |       82.9787  |  8.028 |  21.2766  | 51.3298 |
| Experian PLC                    | EXPN     | EXPN.L         |  56.3916  |  84.0426  |  5.01702  | 32.9787  |      15.699 |       52.1277  |  5.301 |  36.1702  | 51.3298 |
| Linde PLC                       | LIN      | LIN.F          |  53.3312  |  80.8511  |  4.63611  | 36.1702  |      15.567 |       50       |  5.081 |  37.234   | 51.0638 |
| Duke Energy Corporation         | DUK      | DUK            |  58.5573  |  86.1702  |  3.30147  | 45.7447  |      13.1   |       41.4894  |  6.167 |  29.7872  | 50.7979 |
| E.ON SE                         | EOAN     | EOAN.F         |  11.6624  |   7.44681 |  0.421809 | 94.6809  |       8.718 |        8.51064 |  0.992 |  91.4894  | 50.5319 |
| Charter Communications Inc.     | CHTR     | CHTR           |  41.6249  |  72.3404  |  2.84255  | 55.3191  |      12.094 |       34.0426  |  4.605 |  40.4255  | 50.5319 |
| Croda International PLC         | CRDA     | CRDA.L         |  49.3411  |  75.5319  |  7.66486  | 23.4043  |      29.214 |       80.8511  |  7.768 |  22.3404  | 50.5319 |
| Volkswagen AG                   | VOW3     | VOW3.F         |   9.54774 |   5.31915 |  0.548834 | 91.4894  |       9.909 |       15.9574  |  1.17  |  88.2979  | 50.266  |

## References

1. Jason Fernando. (june 29, 2021). _Price-to-Earnings (P/E) Ratio Definition and Examples_. Investopedia. Retrieved on july 10, 2021 from https://www.investopedia.com/terms/p/price-earningsratio.asp

[1]: https://www.investopedia.com/terms/p/price-earningsratio.asp

2. Marshall Hargrave. (may 6, 2021). _Price-to-Sales Ratio (P/S Ratio) Definition_. Investopedia. Retrieved on july 10, 2021 from https://www.investopedia.com/terms/p/price-to-salesratio.asp

[2]: https://www.investopedia.com/terms/p/price-to-salesratio.asp

3. Adam Hayes. (march 25, 2021). _Enterprise Multiple Definition_. Investopedia. Retrieved on july 10, 2021 from https://www.investopedia.com/terms/e/ev-ebitda.asp

[3]: https://www.investopedia.com/terms/e/ev-ebitda.asp

4. Marshall Hargrave. (february 27, 2021). _Enterprise-Value-to-Revenue Multiple – EV/R Definition_. Investopedia. Retrieved on july 10, 2021 https://www.investopedia.com/terms/e/ev-revenue-multiple.asp

[4]: https://www.investopedia.com/terms/e/ev-revenue-multiple.asp