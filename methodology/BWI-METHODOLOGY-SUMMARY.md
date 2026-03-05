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
| D1 | Burden ratio (% of income) | 55% (attainment) | 85% (crisis) | Lower is better | 2024 |
| D2a | Delinquency rate (90+ days, %) | 1.5% (attainment) | 12% (crisis) | Lower is better | 2024 |
| D2b | Net worth (median, $1000s) | $0K (crisis) | $200K (attainment) | Higher is better | 2024 |
| D3 | LFPR, 25-54 | 62% (crisis) | 88% (attainment) | Higher is better | 2024 |
| D4a | YPLL per 100K | 3,500 (attainment) | 9,000 (crisis) | Lower is better | 2024 |
| D4b | Disability rate, 25-54 | 5% (attainment) | 18% (crisis) | Lower is better | 2024 |

**Reading the table**: For "lower is better" indicators, the low value is attainment (score 100) and the high value is crisis (score 0). For "higher is better" indicators, it's reversed. Values between are linearly interpolated. All scores clamped to [1, 99] to prevent log(0) in geometric mean.

### OECD-Benchmarked Bounds (Comparative)

Ceiling values shift to reflect conditions in top-performing OECD nations (Denmark, Finland, etc.). Floor remains US crisis threshold.

| Domain | Indicator | Floor | OECD Ceiling | Data Year |
|--------|-----------|---|---|---|
| D1 | Burden ratio | 85% (crisis) | 32% (OECD attainment) | 2023 |
| D2a | Delinquency rate | 12% (crisis) | 1% (OECD attainment) | 2023 |
| D2b | Net worth (median, $1000s) | $0K (crisis) | $200K (OECD attainment) | 2023 |
| D3 | LFPR, 25-54 | 62% (crisis) | 88% (OECD attainment) | 2023 |
| D4a | YPLL per 100K | 9,000 (crisis) | 5,000 (OECD attainment) | 2023 |
| D4b | Disability rate, 25-54 | 18% (crisis) | 6% (OECD attainment) | 2023 |

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

Q1:  2.5   (crisis across all domains)
Q2: 39.6   (some stability in D3/D4, pressure in D1/D2)
Q3: 74.5   (functional but precarious)
Q4: 95.2   (stable, minor vulnerabilities)
Q5: 99.0   (full attainment)
```

The gap between Q1 and Q5 shows that the top and bottom quintiles are living in different economies.

## Parallel Tracks (Not in Composite)

These measures complement BWI but are not aggregated into the composite:

- **Safety**: BJS National Crime Victimization Survey (violent crime, property crime rates)
- **Sentiment**: University of Michigan Consumer Sentiment Index (FRED: UMCSENT)
- **Despair**: Overdose mortality + suicide mortality (CDC WONDER)

These tracks show psychological and behavioral dimensions that quantify the lived experience beyond pure material conditions.

## Known Data Limitations

### D1 Burden Component Decomposition (Post-2008 Divergence)

The D1 burden ratio is computed from BLS Consumer Expenditure Survey aggregate tables. We also present a five-category decomposition (Housing, Healthcare, Food, Transportation, Childcare) for narrative clarity. These two data series diverge starting in 2008:

| Year | D1 Aggregate | Component Sum | Gap |
|------|-------------|---------------|-----|
| 1990 | 54.6% | 54.6% | 0.0 |
| 2000 | 55.3% | 55.3% | 0.0 |
| 2008 | 56.5% | 60.5% | 4.0 |
| 2015 | 57.3% | 61.3% | 4.0 |
| 2020 | 57.0% | 60.7% | 3.7 |
| 2024 | 58.6% | 61.6% | 3.0 |

**Cause**: The childcare/education component in CEX underwent methodology changes around 2008, including reclassification of education-related expenditures and expanded coverage of formal childcare arrangements. The D1 aggregate series maintains structural consistency across the full time range; the component-level series reflects these methodology shifts.

**Design decision**: The D1 aggregate (58.6% in 2024) is the authoritative value used in all BWI computations. Component-level data is presented as the "five biggest cost categories" for illustrative purposes — it shows directional trends accurately (housing up, food down, etc.) but should not be expected to sum exactly to the D1 aggregate in post-2008 years. We chose to preserve structural consistency in the composite indicator rather than force reconciliation against component series that changed methodology mid-stream. We cannot plan around external methodology changes; we can only enforce structural consistency in our own metric.

### CEX Q1 Composition

The lowest income quintile (Q1) in CEX data includes elderly households on fixed income, students, and temporarily low-income households. This inflates the apparent burden ratio relative to a permanent-income concept. This is a known limitation of all CEX-based poverty research and applies equally across all time periods, so trend comparisons remain valid.

## Revision Protocol

Bounds and aggregation methods are fixed for multi-year comparability. If data sources change or new research suggests different bounds, that becomes version 2.0 with full documentation of the change.

---

For specific data source URLs, series IDs, and frequency, see [../data/DATA-SOURCES.md](../data/DATA-SOURCES.md).
