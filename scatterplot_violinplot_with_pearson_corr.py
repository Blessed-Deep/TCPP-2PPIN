import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def corr_func(x, y, **kwargs):
    corr_coef = x.corr(y)
    ax = plt.gca()
    ax.annotate(f"{corr_coef:.2f}", xy=(0.5, 0.5), xycoords=ax.transAxes, fontsize=35, ha='center', va='center')

# Load your DataFrame
corona_scaled = pd.read_excel("outputs/corona_centrality_measures/corona_data_for_analysis/corona_centrality_scaled_data.xlsx")
influenza_scaled = pd.read_excel("outputs/influenza_centrality_measures/influenza_data_for_analysis/influenza_centrality_scaled_data.xlsx")

corona_scaled = corona_scaled.drop(['Node', 'corona_nodes'], axis=1)
influenza_scaled = influenza_scaled.drop(['Node', 'influenza_nodes'], axis=1)

# Rename the large name for better visualition 
corona_scaled.rename(columns={'closeness_centrality': 'clo'}, inplace=True)
corona_scaled.rename(columns={'harmonic_centrality': 'har'}, inplace=True)
corona_scaled.rename(columns={'degree_centrality': 'deg'}, inplace=True)
corona_scaled.rename(columns={'decay_centrality': 'dec'}, inplace=True)
corona_scaled.rename(columns={'eccentricity': 'ecc'}, inplace=True)
corona_scaled.rename(columns={'radiality_centrality': 'rad'}, inplace=True)
corona_scaled.rename(columns={'load_centrality': 'load'}, inplace=True)
corona_scaled.rename(columns={'approximate_current_flow_betweenness_centrality': 'aprx_cfb'}, inplace=True)
corona_scaled.rename(columns={'betweenness_centrality': 'bet'}, inplace=True)
corona_scaled.rename(columns={'current_flow_closeness_centrality': 'cfc'}, inplace=True)
corona_scaled.rename(columns={'information_centrality': 'info'}, inplace=True)
corona_scaled.rename(columns={'current_flow_betweenness_centrality': 'cfb'}, inplace=True)
corona_scaled.rename(columns={'eigenvector_centrality': 'eig'}, inplace=True)
corona_scaled.rename(columns={'eigenvector_centrality_numpy': 'eig_np'}, inplace=True)
corona_scaled.rename(columns={'pagerank': 'pagerank'}, inplace=True)
corona_scaled.rename(columns={'second_order_centrality': 'sec_o'}, inplace=True)
corona_scaled.rename(columns={'beta_reach_centrality': 'beta_r'}, inplace=True)
corona_scaled.rename(columns={'katz_centrality': 'katz'}, inplace=True)
corona_scaled.rename(columns={'proximal_betweenness': 'pro'}, inplace=True)
corona_scaled.rename(columns={'communicability_betweenness_centrality': 'comm_b'}, inplace=True)
corona_scaled.rename(columns={'katz_centrality_numpy': 'katz_np'}, inplace=True)
corona_scaled.rename(columns={'subgraph_centrality': 'sub'}, inplace=True)
corona_scaled.rename(columns={'subgraph_centrality_exp': 'sub_exp'}, inplace=True)
corona_scaled.rename(columns={'laplacian_centrality': 'lap'}, inplace=True)

influenza_scaled.rename(columns={'closeness_centrality': 'clo'}, inplace=True)
influenza_scaled.rename(columns={'harmonic_centrality': 'har'}, inplace=True)
influenza_scaled.rename(columns={'degree_centrality': 'deg'}, inplace=True)
influenza_scaled.rename(columns={'decay_centrality': 'dec'}, inplace=True)
influenza_scaled.rename(columns={'eccentricity': 'ecc'}, inplace=True)
influenza_scaled.rename(columns={'radiality_centrality': 'rad'}, inplace=True)
influenza_scaled.rename(columns={'load_centrality': 'load'}, inplace=True)
influenza_scaled.rename(columns={'approximate_current_flow_betweenness_centrality': 'aprx_cfb'}, inplace=True)
influenza_scaled.rename(columns={'betweenness_centrality': 'bet'}, inplace=True)
influenza_scaled.rename(columns={'current_flow_closeness_centrality': 'cfc'}, inplace=True)
influenza_scaled.rename(columns={'information_centrality': 'info'}, inplace=True)
influenza_scaled.rename(columns={'current_flow_betweenness_centrality': 'cfb'}, inplace=True)
influenza_scaled.rename(columns={'eigenvector_centrality': 'eig'}, inplace=True)
influenza_scaled.rename(columns={'eigenvector_centrality_numpy': 'eig_np'}, inplace=True)
influenza_scaled.rename(columns={'pagerank': 'pagerank'}, inplace=True)
influenza_scaled.rename(columns={'second_order_centrality': 'sec_o'}, inplace=True)
influenza_scaled.rename(columns={'beta_reach_centrality': 'beta_r'}, inplace=True)
influenza_scaled.rename(columns={'katz_centrality': 'katz'}, inplace=True)
influenza_scaled.rename(columns={'proximal_betweenness': 'pro'}, inplace=True)
influenza_scaled.rename(columns={'communicability_betweenness_centrality': 'comm_b'}, inplace=True)
influenza_scaled.rename(columns={'katz_centrality_numpy': 'katz_np'}, inplace=True)
influenza_scaled.rename(columns={'subgraph_centrality': 'sub'}, inplace=True)
influenza_scaled.rename(columns={'subgraph_centrality_exp': 'sub_exp'}, inplace=True)
influenza_scaled.rename(columns={'laplacian_centrality': 'lap'}, inplace=True)



dis_deg = ['clo',
           'har',
           'deg',
           'dec',
           'ecc',
           'rad',
           'load',
           'aprx_cfb',
           'bet',
           'cfc',
           'info',
           'cfb']
node_cen = ['eig',
            'eig_np',
            'pagerank',
            'sec_o',
            'beta_r',
            'katz',
            'pro',
            'comm_b',
            'katz_np',
            'sub',
            'sub_exp',
            'lap']


def increase_font_size(*args, **kwargs):
    kwargs['fontsize'] = 35  # Adjust the fontsize as needed
    ax = plt.gca()
    ax.tick_params(axis='both', labelsize=20)  # Increase font size for ticks
    ax.set_xlabel(ax.get_xlabel(), **kwargs)
    ax.set_ylabel(ax.get_ylabel(), **kwargs)

# Create a PairGrid with scatterplots and correlation values

# Distance and Degree based
g1 = sns.PairGrid(corona_scaled, vars=dis_deg)
g1.map_upper(corr_func)  
g1.map_diag(sns.violinplot) 
g1.map_lower(sns.scatterplot)
g1.map(increase_font_size)

g1_filename = "figures/scatterplot_violinplot_with_pearson_corr_values/corona_dis_deg.png"
g1.savefig(g1_filename, dpi=300, bbox_inches='tight')

g2 = sns.PairGrid(influenza_scaled, vars=dis_deg)
g2.map_upper(corr_func) 
g2.map_diag(sns.violinplot) 
g2.map_lower(sns.scatterplot)
g2.map(increase_font_size)

g2_filename = "figures/scatterplot_violinplot_with_pearson_corr_values/influenza_dis_deg.png"
g2.savefig(g2_filename, dpi=300, bbox_inches='tight')

# Other node based centrality
g3 = sns.PairGrid(corona_scaled, vars=node_cen)
g3.map_upper(corr_func) 
g3.map_diag(sns.violinplot)  
g3.map_lower(sns.scatterplot)
g3.map(increase_font_size)

g3_filename = "figures/scatterplot_violinplot_with_pearson_corr_values/corona_node_cen.png"
g3.savefig(g3_filename, dpi=300, bbox_inches='tight')

g4 = sns.PairGrid(influenza_scaled, vars=node_cen)
g4.map_upper(corr_func)  
g4.map_diag(sns.violinplot) 
g4.map_lower(sns.scatterplot)
g4.map(increase_font_size)

g4_filename = "figures/scatterplot_violinplot_with_pearson_corr_values/influenza_node_cen.png"
g4.savefig(g4_filename, dpi=300, bbox_inches='tight')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
