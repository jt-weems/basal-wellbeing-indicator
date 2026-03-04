# BWI Data Sources

Every indicator is built from public, verifiable data. This table lists every source with access details and frequency.

## Domain 1: Economic Reality (Burden Ratio)

| Indicator | Source Agency | Survey/Series | Series ID / URL | Frequency | Years Available |
|-----------|---|---|---|---|---|
| Consumption burden ratio (shelter, food, utilities, transportation) | Bureau of Labor Statistics (BLS) | Consumer Expenditure Survey (CEX) | CWIC (Consumer Wealth Income Consumption) tables; search by quintile | Quarterly | 1988-present |
| | | | Main tables: `https://www.bls.gov/cex/tables.htm` | | |
| | | | Quintile breakouts: `https://www.bls.gov/cex/tables/income.htm` | | |

## Domain 2a: Economic Security (Delinquency)

| Indicator | Source Agency | Survey/Series | Series ID / URL | Frequency | Years Available |
|-----------|---|---|---|---|---|
| Delinquency rate (90+ days past due) | Federal Reserve Bank of New York | Consumer Credit Panel (CCP) | NY Fed SCE: https://www.newyorkfed.org/mediumterm/SCE | Quarterly | 2016-present |
| | | Equifax credit file subset | Details: `https://www.newyorkfed.org/mediumterm/SCE/byincome` | | |
| | | | Download: NY Fed Quarterly Report on Household Debt and Credit | | |

## Domain 2b: Economic Security (Net Worth)

| Indicator | Source Agency | Survey/Series | Series ID / URL | Frequency | Years Available |
|-----------|---|---|---|---|---|
| Median net worth (total assets - debt) | Federal Reserve | Survey of Consumer Finances (SCF) | Triennial: https://www.federalreserve.gov/econresdata/scf/scfindex.htm | Triennial (3-year) | 1989, 1992, 1995, 1998, 2001, 2004, 2007, 2010, 2013, 2016, 2019, 2022 |
| | | | Data download: https://www.federalreserve.gov/econresdata/scf/scfindex.htm | | |
| Median net worth (disaggregated) | Federal Reserve | Distribution of Finances in America (DFA) | Quarterly: https://www.federalreserve.gov/releases/z1/ | Quarterly | 2010-present |
| | | | FRED series: NetWorth by income quintile | | |

## Domain 3: Economic Mobility (Labor Force Participation)

| Indicator | Source Agency | Survey/Series | Series ID / URL | Frequency | Years Available |
|-----------|---|---|---|---|---|
| Labor force participation rate, age 25-54 | Bureau of Labor Statistics (BLS) | Current Population Survey (CPS) | FRED: LNS11300060 (seasonally adjusted) | Monthly | 1948-present |
| | | | Access: https://fred.stlouisfed.org/series/LNS11300060 | | |
| | | | BLS manual: https://www.bls.gov/cps/tables.htm | | |
| | | | Table A-1: Employment status by age group | | |

## Domain 4a: Health (Years of Potential Life Lost)

| Indicator | Source Agency | Survey/Series | Series ID / URL | Frequency | Years Available |
|-----------|---|---|---|---|---|
| Years of Potential Life Lost (YPLL), all-cause, age-adjusted per 100K | Centers for Disease Control & Prevention (CDC) | WONDER Mortality Database | Query tool: https://wonder.cdc.gov/mortSQL.html | Annual | 1968-present (complete) |
| | | National Center for Health Statistics | | | |
| | | | Select: All Causes of Death, age-adjusted, per 100,000 | | |
| | | | Stratify by: Census region, state, or income proxy (if available) | | |
| | | | Download: Compressed Mortality File (CMF) | | |

## Domain 4b: Health (Prime-Age Disability)

| Indicator | Source Agency | Survey/Series | Series ID / URL | Frequency | Years Available |
|-----------|---|---|---|---|---|
| Disability rate, age 25-54 | Census Bureau | Current Population Survey (CPS) Disability Supplement | IPUMS-CPS: https://cps.ipums.org/ | Annual or biennial | 2008-present (varies by year) |
| | | | Direct: https://www.census.gov/topics/health/disability/about.html | | |
| | | | American Time Use Survey (ATUS) disability supplement | | |
| | | | BLS CPS disability data: https://www.bls.gov/cps/ | | |

## Parallel Tracks

### Safety: Crime Victimization

| Indicator | Source Agency | Survey/Series | Series ID / URL | Frequency | Years Available |
|-----------|---|---|---|---|---|
| Violent crime and property crime victimization rates | Bureau of Justice Statistics (BJS) | National Crime Victimization Survey (NCVS) | NCVS Data Tool: https://www.bjs.ojp.usdoj.gov/content/datashare/topicsearch.cfm?topic_id=83 | Annual | 1973-present |
| | | | Trend tables: https://bjs.ojp.usdoj.gov/content/pub/pdf/cv21.pdf | | |

### Sentiment: Consumer Sentiment

| Indicator | Source Agency | Survey/Series | Series ID / URL | Frequency | Years Available |
|-----------|---|---|---|---|---|
| Consumer Sentiment Index | University of Michigan | Surveys of Consumers | FRED: UMCSENT | Monthly | 1978-present |
| | | Institute for Social Research | https://fred.stlouisfed.org/series/UMCSENT | | |

### Despair: Mortality

| Indicator | Source Agency | Survey/Series | Series ID / URL | Frequency | Years Available |
|-----------|---|---|---|---|---|
| Overdose mortality, age-adjusted per 100K | CDC WONDER | National Center for Health Statistics | https://wonder.cdc.gov/mortSQL.html | Annual | 1999-present |
| | | Compressed Mortality File | Select: Overdose (underlying cause ICD-10: X40-X44) | | |
| Suicide mortality, age-adjusted per 100K | CDC WONDER | NCHS | https://wonder.cdc.gov/mortSQL.html | Annual | 1968-present |
| | | Compressed Mortality File | Select: Suicide (underlying cause ICD-10: X60-X84) | | |

## Data Access Notes

- **BLS data**: Most BLS time series accessible via FRED (St. Louis Federal Reserve Economic Data): https://fred.stlouisfed.org/
- **Census/CPS data**: Raw microdata available via IPUMS: https://ipums.org/
- **Federal Reserve**: Financial Accounts of the US (Z.1 release): https://www.federalreserve.gov/releases/z1/
- **CDC WONDER**: Query tool available at https://wonder.cdc.gov/ — no registration required, direct download
- **NY Fed Consumer Credit Panel**: Quarterly summary statistics and working papers at https://www.newyorkfed.org/research/

## Current Data Snapshot (2024)

All data current as of the date this repository was created. Sources are updated on their regular schedules (monthly for BLS, quarterly for Federal Reserve, annual for CDC). Check individual source URLs for the latest release.

---

**For calculation methodology, see [../methodology/BWI-METHODOLOGY-SUMMARY.md](../methodology/BWI-METHODOLOGY-SUMMARY.md)**
