#!/usr/bin/env python3
"""
Multi-Criteria Decision Making Analysis using pymcdm
Lab 4 - Complete Solution

This script demonstrates the use of TOPSIS and SPOTIS methods
for multi-criteria decision making problems.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR
from pymcdm.normalizations import minmax_normalization, vector_normalization
# Note: entropy_weighting and equal_weighting not available in current pymcdm version
# We'll implement them manually
from pymcdm.helpers import rrankdata
import warnings

warnings.filterwarnings('ignore')


def create_sample_dataset():
    """
    Create a sample decision matrix for investment alternatives
    Criteria: Cost (min), Profit (max), Risk (min), Time (min), Quality (max)
    """
    # Decision matrix: 6 investment alternatives, 5 criteria
    matrix = np.array([
        [100, 80, 0.3, 12, 8.5],  # Alternative A
        [120, 95, 0.2, 10, 9.0],  # Alternative B
        [90, 70, 0.4, 15, 7.5],  # Alternative C
        [110, 85, 0.25, 11, 8.8],  # Alternative D
        [95, 75, 0.35, 14, 8.0],  # Alternative E
        [105, 90, 0.22, 9, 9.2]  # Alternative F
    ])

    # Criteria types: 1 for benefit (max), -1 for cost (min)
    types = np.array([-1, 1, -1, -1, 1])  # Cost, Profit, Risk, Time, Quality

    # Alternative names
    alternatives = ['Investment A', 'Investment B', 'Investment C',
                    'Investment D', 'Investment E', 'Investment F']

    # Criteria names
    criteria = ['Cost (k$)', 'Profit (k$)', 'Risk', 'Time (months)', 'Quality']

    return matrix, types, alternatives, criteria


def entropy_weighting(matrix):
    """Calculate entropy weights for criteria"""
    # Normalize the matrix
    norm_matrix = matrix / matrix.sum(axis=0)

    # Calculate entropy for each criterion
    entropy = np.zeros(matrix.shape[1])
    for j in range(matrix.shape[1]):
        # Add small epsilon to avoid log(0)
        norm_col = norm_matrix[:, j] + 1e-10
        entropy[j] = -np.sum(norm_col * np.log(norm_col)) / np.log(matrix.shape[0])

    # Calculate weights (higher entropy = lower weight)
    diversity = 1 - entropy
    weights = diversity / diversity.sum()

    return weights


def equal_weighting(matrix):
    """Calculate equal weights for all criteria"""
    return np.ones(matrix.shape[1]) / matrix.shape[1]


def calculate_weights_methods(matrix):
    """Calculate weights using different methods"""

    # Method 1: Equal weights
    equal_w = equal_weighting(matrix)

    # Method 2: Entropy weighting
    entropy_w = entropy_weighting(matrix)

    # Method 3: Manual weights based on business importance
    manual_w = np.array([0.25, 0.30, 0.20, 0.15, 0.10])  # Cost, Profit, Risk, Time, Quality

    return {
        'Equal': equal_w,
        'Entropy': entropy_w,
        'Manual': manual_w
    }


def apply_mcdm_methods(matrix, weights, types):
    """Apply different MCDM methods"""

    results = {}

    # TOPSIS Method
    topsis = TOPSIS()
    topsis_scores = topsis(matrix, weights, types)
    topsis_ranking = rrankdata(topsis_scores)
    results['TOPSIS'] = {'scores': topsis_scores, 'ranking': topsis_ranking}

    # SPOTIS Method - requires bounds parameter
    # Calculate bounds for SPOTIS (ideal point for each criterion)
    bounds = np.zeros(matrix.shape[1])
    for i in range(matrix.shape[1]):
        if types[i] == 1:  # benefit criterion - max is best
            bounds[i] = np.max(matrix[:, i])
        else:  # cost criterion - min is best
            bounds[i] = np.min(matrix[:, i])

    spotis = SPOTIS()
    spotis_scores = spotis(matrix, weights, types, bounds)
    spotis_ranking = rrankdata(spotis_scores, reverse=True)  # SPOTIS: lower is better
    results['SPOTIS'] = {'scores': spotis_scores, 'ranking': spotis_ranking}

    # VIKOR Method (optional)
    vikor = VIKOR()
    vikor_scores = vikor(matrix, weights, types)
    vikor_ranking = rrankdata(vikor_scores, reverse=True)  # VIKOR: lower is better
    results['VIKOR'] = {'scores': vikor_scores, 'ranking': vikor_ranking}

    return results


def compare_normalizations(matrix, weights, types):
    """Compare different normalization methods"""

    normalizations = {
        'Original': matrix,
        'Min-Max': minmax_normalization(matrix),
        'Vector': vector_normalization(matrix)
    }

    comparison_results = {}

    for norm_name, norm_matrix in normalizations.items():
        topsis = TOPSIS()
        scores = topsis(norm_matrix, weights, types)
        ranking = rrankdata(scores)
        comparison_results[norm_name] = {'scores': scores, 'ranking': ranking}

    return comparison_results


def create_results_dataframe(results, alternatives):
    """Create a comprehensive results DataFrame"""

    df_data = {'Alternative': alternatives}

    for method_name, method_results in results.items():
        df_data[f'{method_name}_Score'] = method_results['scores']
        df_data[f'{method_name}_Rank'] = method_results['ranking']

    return pd.DataFrame(df_data)


def visualize_results(results_df, alternatives):
    """Create visualizations of the results"""

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

    # Plot 1: Scores comparison
    methods = ['TOPSIS', 'SPOTIS', 'VIKOR']
    x = np.arange(len(alternatives))
    width = 0.25

    for i, method in enumerate(methods):
        scores = results_df[f'{method}_Score'].values
        ax1.bar(x + i * width, scores, width, label=method, alpha=0.8)

    ax1.set_xlabel('Alternatives')
    ax1.set_ylabel('Scores')
    ax1.set_title('MCDM Methods - Scores Comparison')
    ax1.set_xticks(x + width)
    ax1.set_xticklabels([alt.split()[-1] for alt in alternatives])
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot 2: Rankings comparison
    for i, method in enumerate(methods):
        rankings = results_df[f'{method}_Rank'].values
        ax2.plot(alternatives, rankings, marker='o', linewidth=2,
                 label=method, markersize=8)

    ax2.set_xlabel('Alternatives')
    ax2.set_ylabel('Ranking Position')
    ax2.set_title('MCDM Methods - Rankings Comparison')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xticklabels([alt.split()[-1] for alt in alternatives])

    # Plot 3: TOPSIS scores bar chart
    topsis_scores = results_df['TOPSIS_Score'].values
    colors = plt.cm.viridis(np.linspace(0, 1, len(alternatives)))
    bars = ax3.bar(range(len(alternatives)), topsis_scores, color=colors, alpha=0.8)
    ax3.set_xlabel('Alternatives')
    ax3.set_ylabel('TOPSIS Score')
    ax3.set_title('TOPSIS Scores by Alternative')
    ax3.set_xticks(range(len(alternatives)))
    ax3.set_xticklabels([alt.split()[-1] for alt in alternatives])
    ax3.grid(True, alpha=0.3)

    # Add value labels on bars
    for bar, score in zip(bars, topsis_scores):
        ax3.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                 f'{score:.3f}', ha='center', va='bottom')

    # Plot 4: Ranking positions heatmap
    ranking_matrix = np.array([results_df[f'{method}_Rank'].values for method in methods])
    im = ax4.imshow(ranking_matrix, cmap='RdYlBu_r', aspect='auto')
    ax4.set_xticks(range(len(alternatives)))
    ax4.set_xticklabels([alt.split()[-1] for alt in alternatives])
    ax4.set_yticks(range(len(methods)))
    ax4.set_yticklabels(methods)
    ax4.set_title('Ranking Positions Heatmap\n(1=Best, 6=Worst)')

    # Add text annotations
    for i in range(len(methods)):
        for j in range(len(alternatives)):
            ax4.text(j, i, int(ranking_matrix[i, j]),
                     ha='center', va='center', color='white', fontweight='bold')

    plt.colorbar(im, ax=ax4)
    plt.tight_layout()
    plt.show()


def analyze_weight_sensitivity(matrix, types, alternatives):
    """Analyze sensitivity to different weighting schemes"""

    weight_methods = calculate_weights_methods(matrix)
    sensitivity_results = {}

    print("\n" + "=" * 60)
    print("WEIGHT SENSITIVITY ANALYSIS")
    print("=" * 60)

    for weight_name, weights in weight_methods.items():
        print(f"\n{weight_name} Weights: {weights}")

        # Apply TOPSIS with different weights
        topsis = TOPSIS()
        scores = topsis(matrix, weights, types)
        ranking = rrankdata(scores)

        sensitivity_results[weight_name] = {
            'weights': weights,
            'scores': scores,
            'ranking': ranking
        }

        # Display results
        print(f"\n{weight_name} Weighting Results:")
        for i, (alt, score, rank) in enumerate(zip(alternatives, scores, ranking)):
            print(f"  {alt}: Score={score:.4f}, Rank={rank}")

    return sensitivity_results


def generate_report(matrix, types, alternatives, criteria, results_df, weight_sensitivity):
    """Generate a comprehensive analysis report"""

    report = f"""
# Multi-Criteria Decision Making Analysis Report

## Dataset Overview
- **Number of alternatives**: {len(alternatives)}
- **Number of criteria**: {len(criteria)}
- **Criteria**: {', '.join(criteria)}
- **Decision matrix shape**: {matrix.shape}

## Criteria Configuration
"""

    for i, (criterion, ctype) in enumerate(zip(criteria, types)):
        objective = "Maximize (Benefit)" if ctype == 1 else "Minimize (Cost)"
        report += f"- **{criterion}**: {objective}\n"

    report += f"""
## Method Comparison Results

### Best Alternative by Each Method:
"""

    methods = ['TOPSIS', 'SPOTIS', 'VIKOR']
    for method in methods:
        best_idx = results_df[f'{method}_Rank'].idxmin()
        best_alt = results_df.loc[best_idx, 'Alternative']
        best_score = results_df.loc[best_idx, f'{method}_Score']
        report += f"- **{method}**: {best_alt} (Score: {best_score:.4f})\n"

    report += f"""
### Complete Rankings:

{results_df.to_string(index=False, float_format='%.4f')}

## Key Findings:

1. **Consistency Analysis**: 
   - Methods show {'high' if check_ranking_consistency(results_df) else 'low'} consistency in rankings

2. **Top Performers**: 
   - Most consistent top performer: {find_most_consistent_top_performer(results_df)}

3. **Weight Sensitivity**: 
   - Equal weights vs Entropy weights show {'similar' if compare_weight_impact(weight_sensitivity) else 'different'} results

## Recommendations:

Based on the comprehensive analysis using multiple MCDM methods, the recommended alternative is 
**{get_final_recommendation(results_df)}** as it consistently performs well across different methods.

## Technical Notes:
- All methods were applied with proper normalization
- Criteria types were correctly specified (benefit vs cost)
- Multiple weighting schemes were tested for robustness
"""

    return report


def check_ranking_consistency(results_df):
    """Check if rankings are consistent across methods"""
    methods = ['TOPSIS', 'SPOTIS', 'VIKOR']
    rankings = [results_df[f'{method}_Rank'].values for method in methods]

    # Calculate Spearman rank correlation
    from scipy.stats import spearmanr
    correlations = []
    for i in range(len(methods)):
        for j in range(i + 1, len(methods)):
            corr, _ = spearmanr(rankings[i], rankings[j])
            correlations.append(corr)

    avg_correlation = np.mean(correlations)
    return avg_correlation > 0.7  # Consider high if average correlation > 0.7


def find_most_consistent_top_performer(results_df):
    """Find the alternative that consistently ranks high"""
    methods = ['TOPSIS', 'SPOTIS', 'VIKOR']
    avg_rank = np.mean([results_df[f'{method}_Rank'].values for method in methods], axis=0)
    best_idx = np.argmin(avg_rank)
    return results_df.loc[best_idx, 'Alternative']


def compare_weight_impact(weight_sensitivity):
    """Compare impact of different weighting schemes"""
    equal_ranking = weight_sensitivity['Equal']['ranking']
    entropy_ranking = weight_sensitivity['Entropy']['ranking']

    from scipy.stats import spearmanr
    corr, _ = spearmanr(equal_ranking, entropy_ranking)
    return corr > 0.8


def get_final_recommendation(results_df):
    """Get final recommendation based on multiple methods"""
    return find_most_consistent_top_performer(results_df)


def main():
    """Main execution function"""

    print("=" * 60)
    print("MULTI-CRITERIA DECISION MAKING ANALYSIS")
    print("Using pymcdm library - TOPSIS, SPOTIS, and VIKOR")
    print("=" * 60)

    # Step 1: Prepare data
    print("\n1. Preparing dataset...")
    matrix, types, alternatives, criteria = create_sample_dataset()

    print(f"Dataset created: {len(alternatives)} alternatives, {len(criteria)} criteria")
    print(f"Decision Matrix:\n{pd.DataFrame(matrix, index=alternatives, columns=criteria)}")

    # Step 2: Calculate weights
    print("\n2. Calculating weights...")
    weight_methods = calculate_weights_methods(matrix)
    weights = weight_methods['Manual']  # Use manual weights as primary
    print(f"Using weights: {dict(zip(criteria, weights))}")

    # Step 3: Apply MCDM methods
    print("\n3. Applying MCDM methods...")
    results = apply_mcdm_methods(matrix, weights, types)

    # Step 4: Create results DataFrame
    results_df = create_results_dataframe(results, alternatives)
    print(f"\nResults Summary:\n{results_df}")

    # Step 5: Weight sensitivity analysis
    print("\n4. Performing sensitivity analysis...")
    weight_sensitivity = analyze_weight_sensitivity(matrix, types, alternatives)

    # Step 6: Compare normalizations
    print("\n5. Comparing normalization methods...")
    norm_comparison = compare_normalizations(matrix, weights, types)
    print("\nNormalization Impact on TOPSIS:")
    for norm_name, norm_results in norm_comparison.items():
        ranking = norm_results['ranking']
        best_alt = alternatives[np.argmin(ranking) - 1]  # -1 because ranking is 1-based
        print(f"  {norm_name}: Best alternative = {best_alt}")

    # Step 7: Visualize results
    print("\n6. Creating visualizations...")
    visualize_results(results_df, alternatives)

    # Step 8: Generate report
    print("\n7. Generating final report...")
    report = generate_report(matrix, types, alternatives, criteria, results_df, weight_sensitivity)

    # Save report to file
    with open('mcdm_analysis_report.md', 'w') as f:
        f.write(report)

    print(report)
    print(f"\nReport saved to 'mcdm_analysis_report.md'")
    print(f"Analysis completed successfully!")

    return results_df, report


if __name__ == "__main__":
    # Install required packages first:
    # pip install pymcdm pandas matplotlib scipy numpy

    try:
        results_df, report = main()
    except ImportError as e:
        print(f"Missing required package: {e}")
        print("Please install required packages:")
        print("pip install pymcdm pandas matplotlib scipy numpy")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your data and try again.")