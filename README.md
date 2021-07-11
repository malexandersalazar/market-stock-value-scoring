# Just another market stock value scoring algorithm

There are as many strategies for selecting stocks for an investment portfolio as there are personalities in the world. The present algorithm is only intended to share a basic example using publicly available business information.

## Investment disclaimer

This project is distributed for general informational and educational purposes only and is not intended to constitute investment advice.

## Glosary

**Symbol:** A stock symbol is a unique series of letters assigned to a security for trading purposes. Stocks listed on the New York Stock Exchange (NYSE) can have four or fewer letters. Nasdaq-listed securities can have up to five characters. Symbols are just a shorthand way of describing a company's stock, so there is no significant difference between those that have three letters and those that have four or five. Stock symbols are also known as ticker symbols. [Learn more][1]

**PriceToEarningsRatio:** The price-to-earnings ratio (P/E ratio) is the ratio for valuing a company that measures its current share price relative to its per-share earnings (EPS). The price-to-earnings ratio is also sometimes known as the price multiple or the earnings multiple. [Learn more][2]

**PriceToSalesRatio:** The price-to-sales ratio (Price/Sales or P/S) is calculated by taking a company's market capitalization (the number of outstanding shares multiplied by the share price) and divide it by the company's total sales or revenue over the past 12 months. The lower the P/S ratio, the more attractive the investment. [Learn more][3]

**EV_EBITDA:** The enterprise value (EV) to the earnings before interest, taxes, depreciation, and amortization (EBITDA) ratio varies by industry. EBITDA measures a firm's overall financial performance, while EV determines the firm's total value. [Learn more][4]

**EV_R:** The enterprise value-to-revenue (EV/R) multiple helps compare a company’s revenues to its enterprise value. The lower the better, in that, a lower EV/R multiple signals a company is undervalued. The EV/R multiple is also often used to determine a company's valuation in the case of a potential acquisition. It's also called the enterprise value-to-sales multiple. [Learn more][5]

## Usage

Just copy the PY file and off you go.

> python run.py

## Prerequisites

* Python (>= 3.8.5)
* yfinance (>= 0.1.62)
* pytickersymbols (>= 1.4.3)

## Results

| Company                         | Symbol   | Yahoo Symbol   |       P/E |    P/E PC |       P/S |   P/S PC |   EV/EBITDA |   EV/EBITDA PC |   EV/R |   EV/R PC |   Score |
|:--------------------------------|:---------|:---------------|----------:|----------:|----------:|---------:|------------:|---------------:|-------:|----------:|--------:|
| Costco Wholesale Corporation    | COST     | COST           |  42.1689  |  73.6842  |  0.977768 | 83.1579  |      20.052 |       64.2105  |  0.932 |  92.6316  | 78.4211 |
| Wm Morrison Supermarkets PLC    | MRW      | MRW.L          |  66.225   |  91.5789  |  0.362737 | 95.7895  |      11.203 |       22.1053  |  0.499 |  98.4211  | 76.9737 |
| adidas AG                       | ADS      | ADS.F          |  64.4007  |  89.4737  |  2.97905  | 49.4737  |      31.882 |       83.1579  |  3.048 |  60       | 70.5263 |
| JD Sports Fashion plc           | JD       | JD.L           |  41.6087  |  71.5789  |  1.60081  | 69.4737  |      16.822 |       54.7368  |  1.709 |  75.7895  | 67.8947 |
| United Parcel Service Inc.      | UPS      | UPS            |  36.1229  |  65.2632  |  2.09477  | 62.1053  |      21.231 |       69.4737  |  2.194 |  70.5263  | 66.8421 |
| Walgreens Boots Alliance Inc.   | WBA      | WBA            |  17.9244  |  16.8421  |  0.280553 | 98.9474  |      15.626 |       50.5263  |  0.56  |  95.7895  | 65.5263 |
| Johnson Matthey PLC             | JMAT     | JMAT.L         |  29.718   |  48.4211  |  0.390449 | 94.7368  |      10.197 |       17.8947  |  0.432 | 100       | 65.2632 |
| Amazon.com Inc.                 | AMZN     | AMZN           |  70.761   |  93.6842  |  4.47535  | 37.8947  |      32.918 |       84.2105  |  4.49  |  43.1579  | 64.7368 |
| Ford Motor Company              | F        | F              |  14.5674  |  11.5789  |  0.447873 | 92.6316  |      21.708 |       71.5789  |  1.422 |  82.1053  | 64.4737 |
| Ferguson PLC                    | FERG     | FERG.L         |  34.1471  |  57.8947  |  1.04231  | 80       |      11.846 |       29.4737  |  1.018 |  89.4737  | 64.2105 |
| Vodafone Group PLC              | VOD      | VOD            | 333.4     |  97.8947  |  1.06052  | 78.9474  |       9.491 |       11.5789  |  2.613 |  64.2105  | 63.1579 |
| Walmart Inc.                    | WMT      | WMT.F          |  32.4072  |  53.6842  |  0.591159 | 88.4211  |       9.513 |       12.6316  |  0.67  |  94.7368  | 62.3684 |
| NEXT PLC                        | NXT      | NXT.L          |  35.3312  |  62.1053  |  2.94907  | 50.5263  |      25.66  |       78.9474  |  3.395 |  53.6842  | 61.3158 |
| Starbucks Corporation           | SBUX     | SBUX           | 138.363   |  96.8421  |  5.80534  | 27.3684  |      44.572 |       91.5789  |  6.346 |  28.4211  | 61.0526 |
| CRH PLC                         | CRH      | CRH            |  35.5712  |  64.2105  |  1.4307   | 72.6316  |      11.879 |       30.5263  |  1.688 |  76.8421  | 61.0526 |
| Rentokil Initial PLC            | RTO      | RTO.F          |  49.9145  |  78.9474  |  4.06042  | 41.0526  |      21.159 |       68.4211  |  3.939 |  47.3684  | 58.9474 |
| Bunzl PLC                       | BNZL     | BNZL.L         |  19.9221  |  22.1053  |  0.852562 | 84.2105  |      12.777 |       36.8421  |  1.017 |  90.5263  | 58.4211 |
| DS Smith PLC                    | SMDS     | SMDS.L         |  30.2979  |  51.5789  |  0.981817 | 82.1053  |       9.549 |       13.6842  |  1.283 |  83.6842  | 57.7632 |
| Caterpillar Inc.                | CAT      | CAT            |  34.7649  |  61.0526  |  2.76976  | 55.7895  |      18.827 |       61.0526  |  3.419 |  52.6316  | 57.6316 |
| Ashtead Group PLC               | AHT      | AHT.F          |  37.422   |  68.4211  |  1.90932  | 63.1579  |      12.17  |       32.6316  |  2.526 |  65.2632  | 57.3684 |
| Exelon Corporation              | EXC      | EXC            |  40.4595  |  70.5263  |  1.28386  | 74.7368  |       9.937 |       16.8421  |  2.504 |  66.3158  | 57.1053 |
| Accenture PLC                   | ACN      | ACN            |  36.9965  |  67.3684  |  4.35047  | 38.9474  |      23.745 |       74.7368  |  3.945 |  46.3158  | 56.8421 |
| Bayerische Motoren Werke AG     | BMW      | BMW.F          |  15.3246  |  13.6842  |  0.558448 | 89.4737  |      14.33  |       44.2105  |  1.464 |  80       | 56.8421 |
| Koninklijke Ahold Delhaize N.V. | AD       | AD.AS          |  20.6016  |  29.4737  |  0.347659 | 96.8421  |       7.719 |        4.21053 |  0.518 |  96.8421  | 56.8421 |
| Smiths Group PLC                | SMIN     | SMIN.L         |  25.9776  |  41.0526  |  2.61398  | 56.8421  |      21.118 |       67.3684  |  3.041 |  61.0526  | 56.5789 |
| NIKE Inc.                       | NKE      | NKE.F          |  45.1051  |  74.7368  |  4.82126  | 32.6316  |      26.715 |       80       |  4.778 |  38.9474  | 56.5789 |
| FedEx Corporation               | FDX      | FDX.F          |  26.2323  |  42.1053  |  0.792023 | 85.2632  |       8.257 |        6.31579 |  1.156 |  88.4211  | 55.5263 |
| Pearson PLC                     | PSON     | PSON.L         |  20.0341  |  23.1579  |  1.82859  | 65.2632  |      18.793 |       60       |  2.019 |  72.6316  | 55.2632 |
| AVEVA Group plc                 | AVV      | AVV.L          | 347.257   |  98.9474  | 14.4051   | 10.5263  |      74.339 |       97.8947  | 14.09  |  11.5789  | 54.7368 |
| Dow Inc.                        | DOW      | DOW            |  23.8308  |  38.9474  |  1.15905  | 77.8947  |      10.992 |       21.0526  |  1.541 |  78.9474  | 54.2105 |
| Daimler AG                      | DAI      | DAI.F          |   9.9959  |   6.31579 |  0.495801 | 91.5789  |      12.299 |       33.6842  |  1.283 |  83.6842  | 53.8158 |
| Intertek Group PLC              | ITRK     | ITRK.L         |  36.7585  |  66.3158  |  3.29767  | 46.3158  |      16.6   |       52.6316  |  3.536 |  49.4737  | 53.6842 |
| Tesla Inc.                      | TSLA     | TSLA           | 658.267   | 100       | 17.6088   |  7.36842 |     138.28  |       98.9474  | 17.51  |   8.42105 | 53.6842 |
| Target Corporation              | TGT      | TGT            |  20.2956  |  26.3158  |  1.25305  | 75.7895  |      11.538 |       27.3684  |  1.272 |  85.2632  | 53.6842 |
| Netflix Inc.                    | NFLX     | NFLX           |  64.8651  |  90.5263  |  9.00494  | 15.7895  |      42.652 |       89.4737  |  9.228 |  18.9474  | 53.6842 |
| Booking Holdings Inc.           | BKNG     | BKNG           | 128.354   |  95.7895  | 15.9516   |  8.42105 |     172.747 |      100       | 16.85  |   9.47368 | 53.4211 |
| Deutsche Post AG                | DPW      | DPW.F          |  19.126   |  18.9474  |  1.02736  | 81.0526  |      11.488 |       26.3158  |  1.203 |  86.3158  | 53.1579 |
| Spirax-Sarco Engineering PLC    | SPX      | SPX.L          |  59.6678  |  88.4211  |  8.65981  | 17.8947  |      34.705 |       86.3158  |  8.5   |  20       | 53.1579 |
| Halma PLC                       | HLMA     | HLMA.L         |  51.7724  |  82.1053  |  7.99207  | 22.1053  |      34.106 |       85.2632  |  8.065 |  22.1053  | 52.8947 |
| Tesco PLC                       | TSCO     | TSCO.L         |   2.94913 |   3.15789 |  0.317485 | 97.8947  |       9.334 |       10.5263  |  0.499 |  98.4211  | 52.5    |
| Siemens AG                      | SIE      | SIE.F          |  18.1338  |  17.8947  |  1.81355  | 66.3158  |      16.873 |       55.7895  |  2.242 |  69.4737  | 52.3684 |
| PayPal Holdings Inc.            | PYPL     | PYPL           |  68.4161  |  92.6316  | 15.4211   |  9.47368 |      67.031 |       95.7895  | 14.582 |  10.5263  | 52.1053 |
| salesforce.com Inc.             | CRM      | CRM            |  51.6677  |  81.0526  | 10.1533   | 14.7368  |      63.606 |       94.7368  |  9.892 |  16.8421  | 51.8421 |
| Linde PLC                       | LIN      | LIN.F          |  53.3312  |  84.2105  |  4.63611  | 35.7895  |      15.567 |       49.4737  |  5.081 |  36.8421  | 51.5789 |
| The Home Depot Inc.             | HD       | HD             |  23.4794  |  35.7895  |  2.42282  | 58.9474  |      15.161 |       48.4211  |  2.677 |  62.1053  | 51.3158 |
| Lowe's Companies Inc.           | LOW      | LOW            |  21.3056  |  31.5789  |  1.46355  | 70.5263  |      11.418 |       25.2632  |  1.671 |  77.8947  | 51.3158 |
| Croda International PLC         | CRDA     | CRDA.L         |  49.3411  |  77.8947  |  7.66486  | 23.1579  |      30.859 |       82.1053  |  8.206 |  21.0526  | 51.0526 |
| General Dynamics Corporation    | GD       | GD             |  17.2927  |  15.7895  |  1.41199  | 73.6842  |      12.962 |       40       |  1.719 |  74.7368  | 51.0526 |
| Duke Energy Corporation         | DUK      | DUK            |  58.5573  |  87.3684  |  3.30147  | 45.2632  |      13.1   |       41.0526  |  6.167 |  29.4737  | 50.7895 |
| Honeywell International Inc.    | HON      | HON            |  34.3448  |  60       |  4.77555  | 33.6842  |      21.374 |       70.5263  |  5.011 |  37.8947  | 50.5263 |
| E.ON SE                         | EOAN     | EOAN.F         |  11.6624  |   7.36842 |  0.421809 | 93.6842  |       8.718 |        8.42105 |  0.992 |  91.5789  | 50.2632 |
| Experian PLC                    | EXPN     | EXPN.L         |  46.6349  |  75.7895  |  5.04225  | 31.5789  |      19.298 |       62.1053  |  5.787 |  31.5789  | 50.2632 |
| Charter Communications Inc.     | CHTR     | CHTR           |  41.6249  |  72.6316  |  2.84255  | 54.7368  |      12.094 |       31.5789  |  4.605 |  41.0526  | 50      |

## References

1. Adam Hayes. (december 28, 2020). _Stock Symbol (Ticker) Definition_. Investopedia. Retrieved on july 11, 2021 from https://www.investopedia.com/terms/s/stocksymbol.asp

[1]: https://www.investopedia.com/terms/s/stocksymbol.asp

2. Jason Fernando. (june 29, 2021). _Price-to-Earnings (P/E) Ratio Definition and Examples_. Investopedia. Retrieved on july 10, 2021 from https://www.investopedia.com/terms/p/price-earningsratio.asp

[2]: https://www.investopedia.com/terms/p/price-earningsratio.asp

3. Marshall Hargrave. (may 6, 2021). _Price-to-Sales Ratio (P/S Ratio) Definition_. Investopedia. Retrieved on july 10, 2021 from https://www.investopedia.com/terms/p/price-to-salesratio.asp

[3]: https://www.investopedia.com/terms/p/price-to-salesratio.asp

4. Adam Hayes. (march 25, 2021). _Enterprise Multiple Definition_. Investopedia. Retrieved on july 10, 2021 from https://www.investopedia.com/terms/e/ev-ebitda.asp

[4]: https://www.investopedia.com/terms/e/ev-ebitda.asp

5. Marshall Hargrave. (february 27, 2021). _Enterprise-Value-to-Revenue Multiple – EV/R Definition_. Investopedia. Retrieved on july 10, 2021 https://www.investopedia.com/terms/e/ev-revenue-multiple.asp

[5]: https://www.investopedia.com/terms/e/ev-revenue-multiple.asp