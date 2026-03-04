# Basal Wellbeing Indicator (BWI)

A composite measure of household-level basic needs attainment in the United States. This is research infrastructure, not a policy advocacy tool.

## What Is BWI?

The Basal Wellbeing Indicator measures whether Americans have the economic foundation to meet basic needs: stable housing, food security, healthcare access, and economic security. It answers one question: *How many people have the material preconditions for functional participation in society?*

BWI is built on open, verifiable data. Every source is public. Every bound is defensible. Every calculation is reproducible. Go check the work.

## Four Domains

**D1 | Economic Reality** (Income adequacy)
- Indicator: Consumption burden ratio (essential vs. discretionary spending)
- Data: BLS Consumer Expenditure Survey by quintile
- What it measures: What fraction of household income goes to shelter, food, utilities, transportation?

**D2 | Economic Security** (Stability & net worth)
- Indicators: Delinquency rate (90+ days) + net worth
- Data: NY Fed Consumer Credit Panel + Federal Reserve SCF/DFA
- What it measures: Can households absorb a $500 emergency? Do they have savings?

**D3 | Economic Mobility** (Labor market attachment)
- Indicator: Prime-age labor force participation rate (25-54)
- Data: BLS Current Population Survey
- What it measures: What fraction of working-age Americans are employed or seeking work?

**D4 | Health** (Mortality & disability)
- Indicators: Years of potential life lost (age-adjusted) + prime-age disability rate
- Data: CDC WONDER + Census CPS disability supplement
- What it measures: Is the population aging out of productive years early? Are people disabled?

## The Two Scales

**US-Normed** (100 = meeting basic needs by American standards)
- Reference: Q4 (top quintile) ≈ 95 in 2024
- Q1 (bottom quintile) ≈ 2.5 in 2024
- Same economy. Two completely different lived experiences.

**OECD-Benchmarked** (100 = conditions achieved by best OECD nations)
- Reference: Conditions in top-performing OECD countries (Denmark, Finland, etc.)
- Shows where US stands relative to international peer standard
- Useful for long-term structural comparison

## Methodology Snapshot

1. **Normalization**: Each indicator normalized to 0–100 using theoretically grounded bounds (floor = crisis, ceiling = full attainment)
2. **Aggregation**: Geometric mean within domains, geometric mean across domains
3. **Geometric mean rationale**: Prevents compensability. A high score in one domain cannot mask a crisis in another. Reflects lived experience: you can't eat financial security.
4. **Decomposition**: Quintile-level analysis to reveal distribution inequality
5. **Parallel tracks** (not in composite): Safety (BJS NCVS), Sentiment (UMich), Despair (overdose + suicide rates)

See [methodology/BWI-METHODOLOGY-SUMMARY.md](methodology/BWI-METHODOLOGY-SUMMARY.md) for full technical detail.

## Key Finding (2024, US-Normed)

| Quintile | BWI Score |
|----------|-----------|
| Q1       | 2.5       |
| Q2       | 18.3      |
| Q3       | 48.7      |
| Q4       | 82.1      |
| Q5       | 99.0      |

The top and bottom quintiles are living in different economies.

## Data Sources

All sources are public, all are verifiable, all are updated on regular schedules:

- **D1 Burden**: BLS Consumer Expenditure Survey (CEX)
- **D2 Delinquency**: NY Federal Reserve Consumer Credit Panel
- **D2 Net Worth**: Federal Reserve Survey of Consumer Finances (SCF) + Distribution of Finances in America (DFA)
- **D3 LFPR**: BLS Current Population Survey
- **D4 YPLL**: CDC WONDER (mortality database)
- **D4 Disability**: Census CPS disability supplement
- **Safety**: Bureau of Justice Statistics National Crime Victimization Survey
- **Sentiment**: University of Michigan Consumer Sentiment Index

See [data/DATA-SOURCES.md](data/DATA-SOURCES.md) for full detail on every series, including URLs and identifiers.

## Why This Matters

Most economic metrics (GDP, unemployment rate, income growth) describe aggregate trends that can obscure severe inequality. BWI directly measures what fraction of the population has the material foundation to function in society — stratified by income quintile so you can see the distribution.

This is not advocacy. This is measurement. You evaluate whether the measures are correct.

## Repository Structure

```
bwi-repo/
├── README.md                           (this file)
├── LICENSE                             (MIT)
├── .gitignore
├── methodology/
│   └── BWI-METHODOLOGY-SUMMARY.md     (technical methodology)
└── data/
    └── DATA-SOURCES.md                 (all sources with identifiers)
```

Python analysis scripts will be added in subsequent releases.

## License

MIT License. Copyright 2026 Taylor Weems.

Built with Claude (Anthropic). Transparency matters.

## Related Content

- **LinkedIn Series**: [Thought leadership on economic measurement and AI adoption](https://www.linkedin.com/in/jt-weems/)
- **Connected Research**: Connections to the Intelligence Transition white paper on economic displacement and AI adoption

---

**Questions?** Open an issue. **Found an error?** Open an issue. **Want to verify the calculation?** Check the methodology, pull the data, run the numbers. This repo exists for scrutiny.
