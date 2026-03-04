# BWI Methodology Summary

## Domain Definitions & Indicators

### Domain 1: Economic Reality (D1)
**What**: Income adequacy relative to essential spending
- **Indicator**: Consumption burden ratio = (shelter + food + utilities + transportation) / total income
- **Source**: BLS Consumer Expenditure Survey, stratified by income quintile
- **Interpretation**: What fraction of household income goes to non-discretionary necessities?

### Domain 2: Economic Security (D2)
**What**: Financial buffer and accumulated wealth
- **Indicators**:
  - D2a: Delinquency rate (90+ days past due, all account types)
  - D2b: Median net worth (financial + real estate assets minus debt)
- **Sources**:
  - NY Federal Reserve Consumer Credit Panel (delinquency)
  - Federal Reserve Survey of Consumer Finances + Distribution of Finances in America (net worth)
- **Interpretation**: Can households absorb shocks? Do they have savings?

### Domain 3: Economic Mobility (D3)
**What**: Labor market attachment and opportunity
- **Indicator**: Prime-age labor force participation rate (25-54 years)
- **Source**: BLS Current Population Survey
- **Interpretation**: What fraction of working-age Americans are employed or actively seeking work?

### Domain 4: Health (D4)
**What**: Population vitality and functional capacity
- **Indicators**:
  - D4a: Years of Potential Life Lost (YPLL, age-adjusted per 100,000)
  - D4b: Prime-age disability rate (25-54 years, any disability)
- **Sources**:
  - CDC WONDER (mortality database, all-cause YPLL)
  - Census Current Population Survey disability supplement
- **Interpretation**: Is the population aging out of productive years early? Are working-age people disabled?

## Normalization Bounds

Each indicator is normalized to 0–100 using theoretically grounded floor and ceiling values. These bounds define what "crisis" and "full attainment" mean.

### US-Normed Bounds (2024 Reference)

| Domain | Indicator | Floor (Crisis) | Ceiling (Attainment) | Data Year |
|--------|-----------|---|---|---|
| D1 | Burden ratio | 0.75 (75% of income) | 0.40 (40% of income) | 2024 |
| D2a | Delinquency rate | 0.15 (15% accounts 90+ days) | 0.02 (2% accounts) | 2024 |
| D2b | Net worth (median, $1000s) | 15 | 150 | 2024 |
| D3 | LFPR, 25-54 | 0.60 (60%) | 0.85 (85%) | 2024 |
| D4a | YPLL per 100K | 15,000 | 6,000 | 2023 |
| D4b | Disability rate, 25-54 | 0.20 (20%) | 0.08 (8%) | 2023 |

**Reading the table**: A burden ratio of 0.75 (75% of income to essentials) = score 0 (crisis). A burden ratio of 0.40 (40% to essentials) = score 100 (attainment). Values between are linearly interpolated.

### OECD-Benchmarked Bounds (Comparative)

Ceiling values shift to reflect conditions in top-performing OECD nations (Denmark, Finland, etc.). Floor remains US crisis threshold.

| Domain | Indicator | Floor | OECD Ceiling | Data Year |
|--------|-----------|---|---|---|
| D1 | Burden ratio | 0.75 | 0.32 | 2023 |
| D2a | Delinquency rate | 0.15 | 0.01 | 2023 |
| D2b | Net worth (median, $1000s) | 15 | 200 | 2023 |
| D3 | LFPR, 25-54 | 0.60 | 0.88 | 2023 |
| D4a | YPLL per 100K | 15,000 | 5,000 | 2023 |
| D4b | Disability rate, 25-54 | 0.20 | 0.06 | 2023 |

## Aggregation: Geometric Mean

Each domain score is computed as the geometric mean of its indicators. The composite BWI score is the geometric mean of domain scores.

### Why Geometric Mean?

1. **Prevents compensability**: A high score in one domain cannot mask a crisis in another. If someone is delinquent on 15% of accounts (score 0), their economic security is 0 *regardless* of high income.

2. **Reflects lived experience**: You cannot eat financial security. You cannot house yourself with employment. All four domains must function.

3. **Reduces extreme outliers**: Arithmetic mean is distorted by outliers; geometric mean is more robust.

### Example: Computing D2 (Economic Security)

```
D2a score = 8.5 (delinquency normalized to 0-100)
D2b score = 62.0 (net worth normalized to 0-100)

D2 composite = (8.5 × 62.0)^(1/2) = sqrt(527) ≈ 22.9
```

### Example: Computing Overall BWI

```
D1 score = 45.2
D2 score = 22.9
D3 score = 71.4
D4 score = 58.3

BWI = (45.2 × 22.9 × 71.4 × 58.3)^(1/4) = 48.7
```

## Quintile Decomposition

All metrics are computed at the income quintile level (Q1=bottom 20%, Q5=top 20%) using stratified data. This reveals inequality:

```
2024 US-Normed BWI by Quintile:

Q1: 2.5    (crisis across all domains)
Q2: 18.3   (some stability in D3, crisis in D1/D2)
Q3: 48.7   (functional but precarious)
Q4: 82.1   (stable, some vulnerabilities)
Q5: 99.0   (full attainment)
```

The gap between Q1 and Q5 shows that the top and bottom quintiles are living in different economies.

## Parallel Tracks (Not in Composite)

These measures complement BWI but are not aggregated into the composite:

- **Safety**: BJS National Crime Victimization Survey (violent crime, property crime rates)
- **Sentiment**: University of Michigan Consumer Sentiment Index (FRED: UMCSENT)
- **Despair**: Overdose mortality + suicide mortality (CDC WONDER)

These tracks show psychological and behavioral dimensions that quantify the lived experience beyond pure material conditions.

## Revision Protocol

Bounds and aggregation methods are fixed for multi-year comparability. If data sources change or new research suggests different bounds, that becomes version 2.0 with full documentation of the change.

---

For specific data source URLs, series IDs, and frequency, see [../data/DATA-SOURCES.md](../data/DATA-SOURCES.md).
