#!/usr/bin/env python3
"""
Basal Wellbeing Indicator (BWI) — Full Computation Pipeline

Takes raw federal data per income quintile, normalizes to 0-100 scale,
aggregates via geometric mean, and outputs quintile + population-weighted scores.

All data sourced from: BLS, Census, CDC, Federal Reserve, NY Fed.
See ../data/DATA-SOURCES.md for complete source citations.

Author: Taylor Weems / PaxCura Advisory (built with Claude, Anthropic)
License: MIT
"""

import math

# =============================================================================
# RAW INDICATOR DATA BY QUINTILE
# =============================================================================
# Years: [2000, 2008, 2015, 2020, 2024]

# Domain 1: Economic Reality — Non-discretionary Burden Ratio (% of income)
# Source: BLS Consumer Expenditure Survey, quintile tables
# Components: Housing + Healthcare + Food + Transportation
D1_BURDEN = {
    'Q1': [82.0, 86.0, 88.0, 85.0, 90.0],
    'Q2': [68.0, 72.0, 73.0, 71.0, 75.0],
    'Q3': [58.0, 60.0, 61.0, 59.0, 62.0],
    'Q4': [49.0, 51.0, 52.0, 50.0, 53.0],
    'Q5': [35.0, 37.0, 38.0, 36.0, 39.0],
}

# Domain 2a: Economic Security — Delinquency Rate (90+ days, % of accounts)
# Source: NY Fed Consumer Credit Panel, stratified by Census Tract income
D2A_DELINQUENCY = {
    'Q1': [7.5, 10.0, 4.5, 3.8, 6.2],
    'Q2': [5.5, 8.0, 3.2, 2.6, 4.5],
    'Q3': [4.0, 5.5, 2.3, 1.9, 3.2],
    'Q4': [2.8, 4.0, 1.5, 1.2, 2.2],
    'Q5': [1.5, 2.5, 0.8, 0.7, 1.2],
}

# Domain 2b: Economic Security — Median Net Worth ($thousands, 2024 dollars)
# Source: Federal Reserve Survey of Consumer Finances (triennial)
D2B_NET_WORTH = {
    'Q1': [8.0, 6.0, 6.5, 13.3, 14.0],
    'Q2': [40.0, 30.0, 35.0, 50.0, 55.0],
    'Q3': [95.0, 80.0, 90.0, 198.9, 230.0],
    'Q4': [180.0, 150.0, 170.0, 350.0, 400.0],
    'Q5': [550.0, 480.0, 520.0, 1017.0, 1200.0],
}

# Domain 3: Economic Mobility — Prime-Age LFPR (%, ages 25-54)
# Source: BLS Current Population Survey, stratified by education (proxy)
D3_LFPR = {
    'Q1': [63.0, 60.0, 56.0, 55.0, 57.0],
    'Q2': [77.0, 75.0, 72.0, 71.0, 73.0],
    'Q3': [81.0, 80.0, 78.0, 77.0, 79.0],
    'Q4': [87.0, 86.0, 85.0, 84.0, 86.0],
    'Q5': [90.0, 89.0, 88.0, 88.0, 89.0],
}

# Domain 4a: Health — YPLL per 100,000 (age-adjusted, all-cause)
# Source: CDC NVSR; education-stratified mortality mapped to YPLL equivalents
D4A_YPLL = {
    'Q1': [7000, 7500, 8500, 9500, 8800],
    'Q2': [5500, 5800, 6500, 7200, 6800],
    'Q3': [4800, 4700, 5200, 5600, 5300],
    'Q4': [3800, 3500, 3600, 4000, 3800],
    'Q5': [3200, 2900, 3000, 3400, 3100],
}

# Domain 4b: Health — Prime-Age Disability Rate (%, ages 25-54)
# Source: BLS CPS disability supplement; ACS validation
D4B_DISABILITY = {
    'Q1': [14.0, 15.0, 16.0, 17.0, 18.0],
    'Q2': [10.0, 11.0, 12.0, 12.5, 13.0],
    'Q3': [7.5, 8.0, 8.5, 8.8, 9.2],
    'Q4': [5.0, 5.2, 5.5, 5.7, 6.0],
    'Q5': [3.5, 3.5, 3.8, 4.0, 4.2],
}

# =============================================================================
# NORMALIZATION BOUNDS
# =============================================================================
# Floor = crisis threshold (score 0). Ceiling = attainment (score 100).
# For 'lower_better': floor is the HIGH value (bad), ceiling is the LOW value (good).
# For 'higher_better': floor is the LOW value (bad), ceiling is the HIGH value (good).

BOUNDS = {
    'D1_burden': {
        # 55% burden = full attainment; 85% = crisis (functional insolvency)
        # Range captures the full span of quintile experience: Q5 at ~39%
        # scores 0.99 (capped), Q1 at ~90% scores 0.01 (capped).
        'floor': 55.0, 'ceiling': 85.0, 'direction': 'lower_better',
    },
    'D2a_delinquency': {
        # 1.5% delinquency = full attainment; 12% = crisis
        # Floor reflects achievable low-delinquency baseline (top quintile tracts).
        'floor': 1.5, 'ceiling': 12.0, 'direction': 'lower_better',
    },
    'D2b_net_worth': {
        # $0 = crisis; $200K = full attainment (robust multi-year buffer)
        # Ceiling at $200K ~ 2.5x median household income.
        'floor': 0.0, 'ceiling': 200.0, 'direction': 'higher_better',
    },
    'D3_lfpr': {
        # 62% participation = severe exclusion; 88% = near-full participation
        # Floor accommodates Q1 education-proxy rates (~55-63%); ceiling
        # reflects BA+ prime-age rates.
        'floor': 62.0, 'ceiling': 88.0, 'direction': 'higher_better',
    },
    'D4a_ypll': {
        # 3500/100K = top OECD benchmark; 9000/100K = severe health failure
        # Wider range captures Q1 mortality divergence (Case & Deaton).
        'floor': 3500.0, 'ceiling': 9000.0, 'direction': 'lower_better',
    },
    'D4b_disability': {
        # 5% = achievable baseline; 18% = demographic health crisis
        # Floor reflects BA+ disability rates; ceiling captures Q1
        # education-proxy rates.
        'floor': 5.0, 'ceiling': 18.0, 'direction': 'lower_better',
    },
}

# =============================================================================
# COMPUTATION FUNCTIONS
# =============================================================================

def normalize(value, floor, ceiling, direction):
    """
    Normalize a raw indicator value to 0-1 scale.
    Clamped to [0.01, 0.99] to avoid log(0) in geometric mean.

    For 'lower_better': a LOW raw value is GOOD.
      score = (ceiling - value) / (ceiling - floor)
      where ceiling is the HIGHER number (crisis end)
      and floor is the LOWER number (attainment end).

    For 'higher_better': a HIGH raw value is GOOD.
      score = (value - floor) / (ceiling - floor)
    """
    if direction == 'lower_better':
        # floor = attainment (lower number), ceiling = crisis (higher number)
        score = (ceiling - value) / (ceiling - floor)
    else:  # higher_better
        score = (value - floor) / (ceiling - floor)
    return max(0.01, min(0.99, score))


def geometric_mean(values):
    """
    Geometric mean of positive values.

    Why geometric mean: prevents compensability. A crisis in any single
    domain (score near 0) pulls the entire composite toward zero.
    You can't offset hunger with a job.
    """
    valid = [v for v in values if v is not None and v > 0]
    if not valid:
        return 0.01
    product = 1.0
    for v in valid:
        product *= v
    return product ** (1.0 / len(valid))


def compute_bwi(year_index):
    """
    Compute BWI for all quintiles at a given year index.
    Returns dict: {quintile: {domain_scores_01, bwi_01, bwi_100}}
    """
    results = {}

    for q in ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']:
        # Normalize each indicator to 0-1
        d1 = normalize(D1_BURDEN[q][year_index], **BOUNDS['D1_burden'])
        d2a = normalize(D2A_DELINQUENCY[q][year_index], **BOUNDS['D2a_delinquency'])

        # Cap net worth at ceiling before normalizing
        nw = min(D2B_NET_WORTH[q][year_index], BOUNDS['D2b_net_worth']['ceiling'])
        d2b = normalize(nw, **BOUNDS['D2b_net_worth'])

        d3 = normalize(D3_LFPR[q][year_index], **BOUNDS['D3_lfpr'])
        d4a = normalize(D4A_YPLL[q][year_index], **BOUNDS['D4a_ypll'])
        d4b = normalize(D4B_DISABILITY[q][year_index], **BOUNDS['D4b_disability'])

        # Domain composites (geometric mean within multi-indicator domains)
        d2 = geometric_mean([d2a, d2b])
        d4 = geometric_mean([d4a, d4b])

        # Overall BWI (geometric mean across 4 domains)
        bwi_01 = geometric_mean([d1, d2, d3, d4])

        results[q] = {
            'indicators_01': {
                'D1': d1, 'D2a': d2a, 'D2b': d2b,
                'D3': d3, 'D4a': d4a, 'D4b': d4b,
            },
            'domains_01': {
                'D1_Economic_Reality': d1,
                'D2_Economic_Security': d2,
                'D3_Economic_Mobility': d3,
                'D4_Health': d4,
            },
            'bwi_01': bwi_01,
            'bwi_100': round(bwi_01 * 100, 1),
        }

    return results


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    YEARS = [2000, 2008, 2015, 2020, 2024]

    print("=" * 78)
    print("BASAL WELLBEING INDICATOR — FULL COMPUTATION")
    print("Scale: 0-100 (100 = basic needs met across all domains)")
    print("Method: Geometric mean aggregation (non-compensatory)")
    print("=" * 78)

    all_results = {}
    for yi, year in enumerate(YEARS):
        all_results[year] = compute_bwi(yi)

    # --- Detailed output for each year ---
    for year in YEARS:
        scores = all_results[year]
        pop_avg = sum(scores[q]['bwi_100'] for q in ['Q1','Q2','Q3','Q4','Q5']) / 5

        print(f"\n{'─' * 78}")
        print(f"  {year}    Population-weighted average: {pop_avg:.1f}")
        print(f"{'─' * 78}")

        # Indicator-level detail
        print(f"  {'':10} {'D1':>7} {'D2a':>7} {'D2b':>7} {'D3':>7} "
              f"{'D4a':>7} {'D4b':>7} | {'D1':>6} {'D2':>6} {'D3':>6} {'D4':>6} | {'BWI':>6}")
        print(f"  {'':10} {'Burden':>7} {'Delinq':>7} {'NW':>7} {'LFPR':>7} "
              f"{'YPLL':>7} {'Disab':>7} | {'':>6} {'':>6} {'':>6} {'':>6} | {'':>6}")
        print(f"  {'─'*10} {'─'*7} {'─'*7} {'─'*7} {'─'*7} "
              f"{'─'*7} {'─'*7}─┤ {'─'*6} {'─'*6} {'─'*6} {'─'*6}─┤ {'─'*6}")

        for q in ['Q5', 'Q4', 'Q3', 'Q2', 'Q1']:
            s = scores[q]
            ind = s['indicators_01']
            dom = s['domains_01']
            print(f"  {q:<10} {ind['D1']*100:>7.1f} {ind['D2a']*100:>7.1f} "
                  f"{ind['D2b']*100:>7.1f} {ind['D3']*100:>7.1f} "
                  f"{ind['D4a']*100:>7.1f} {ind['D4b']*100:>7.1f} | "
                  f"{dom['D1_Economic_Reality']*100:>6.1f} "
                  f"{dom['D2_Economic_Security']*100:>6.1f} "
                  f"{dom['D3_Economic_Mobility']*100:>6.1f} "
                  f"{dom['D4_Health']*100:>6.1f} | "
                  f"{s['bwi_100']:>6.1f}")

        q5q1 = scores['Q5']['bwi_100'] - scores['Q1']['bwi_100']
        print(f"\n  Gap (Q5 - Q1): {q5q1:.1f} points")

    # --- Summary table ---
    print(f"\n\n{'=' * 78}")
    print("SUMMARY: BWI BY QUINTILE ACROSS YEARS (0-100 absolute scale)")
    print(f"{'=' * 78}")
    print(f"\n  {'Year':<8}", end="")
    for q in ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Avg']:
        print(f" {q:>7}", end="")
    print()
    print(f"  {'─'*8}", end="")
    for _ in range(6):
        print(f" {'─'*7}", end="")
    print()

    for year in YEARS:
        scores = all_results[year]
        pop_avg = sum(scores[q]['bwi_100'] for q in ['Q1','Q2','Q3','Q4','Q5']) / 5
        print(f"  {year:<8}", end="")
        for q in ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']:
            print(f" {scores[q]['bwi_100']:>7.1f}", end="")
        print(f" {pop_avg:>7.1f}")

    # --- Raw data reference ---
    print(f"\n\n{'=' * 78}")
    print("RAW INDICATOR VALUES (2024)")
    print(f"{'=' * 78}")
    print(f"\n  {'':10} {'D1%':>7} {'D2a%':>7} {'D2b$K':>7} {'D3%':>7} "
          f"{'D4a':>7} {'D4b%':>7}")
    print(f"  {'─'*10} {'─'*7} {'─'*7} {'─'*7} {'─'*7} {'─'*7} {'─'*7}")
    yi = 4  # 2024
    for q in ['Q5', 'Q4', 'Q3', 'Q2', 'Q1']:
        print(f"  {q:<10} {D1_BURDEN[q][yi]:>7.1f} {D2A_DELINQUENCY[q][yi]:>7.1f} "
              f"{D2B_NET_WORTH[q][yi]:>7.0f} {D3_LFPR[q][yi]:>7.1f} "
              f"{D4A_YPLL[q][yi]:>7.0f} {D4B_DISABILITY[q][yi]:>7.1f}")

    print(f"\n  Normalization bounds:")
    for key, b in BOUNDS.items():
        if b['direction'] == 'lower_better':
            print(f"    {key}: {b['floor']} (attainment) — {b['ceiling']} (crisis)")
        else:
            print(f"    {key}: {b['floor']} (crisis) — {b['ceiling']} (attainment)")

    print(f"\n  Sources: BLS CEX, Fed SCF, NY Fed CCP, BLS CPS, CDC NVSR")
    print(f"  Methodology: ../methodology/BWI-METHODOLOGY-SUMMARY.md")
    print(f"  Data sources: ../data/DATA-SOURCES.md")
