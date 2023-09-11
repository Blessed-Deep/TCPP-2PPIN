import pandas as pd
import matplotlib.pyplot as plt

# Load centrality data from Excel for the two graphs and centrality measures
covid_edge_betweenness_centrality = pd.read_excel("outputs/corona_centrality_measures/modified/edge_betweenness_centrality_modified.xlsx") 
h1n1_edge_betweenness_centrality = pd.read_excel("outputs/influenza_centrality_measures/modified/edge_betweenness_centrality_modified.xlsx")

covid_edge_load_centrality = pd.read_excel("outputs/corona_centrality_measures/modified/edge_load_centrality_modified.xlsx") 
h1n1_edge_load_centrality = pd.read_excel("outputs/influenza_centrality_measures/modified/edge_load_centrality_modified.xlsx")

covid_edge_current_flow_betweenness_centrality = pd.read_excel("outputs/corona_centrality_measures/modified/edge_current_flow_betweenness_centrality_modified.xlsx")  # Replace with your file paths
h1n1_edge_current_flow_betweenness_centrality = pd.read_excel("outputs/influenza_centrality_measures/modified/edge_current_flow_betweenness_centrality_modified.xlsx")

# Choose the top number of nodes to visualize
num_top_nodes = 20

# Plot each centrality measure side by side
plt.figure(figsize=(25, 15))

# COVID Edge Betweenness Centrality
plt.subplot(2, 3, 1)
covid_edge_betweenness_centrality = covid_edge_betweenness_centrality.nlargest(num_top_nodes, 'edge_betweenness_centrality')
plt.scatter(covid_edge_betweenness_centrality['Node'], covid_edge_betweenness_centrality['edge_betweenness_centrality'], color='red')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Edge Betweenness Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Edge Load Centrality
plt.subplot(2, 3, 2)
covid_edge_load_centrality = covid_edge_load_centrality.nlargest(num_top_nodes, 'edge_load_centrality')
plt.scatter(covid_edge_load_centrality['Node'], covid_edge_load_centrality['edge_load_centrality'], color='red')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Edge Load Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Edge Current Flow Betweenness Centrality
plt.subplot(2, 3, 3)
covid_edge_current_flow_betweenness_centrality = covid_edge_current_flow_betweenness_centrality.nlargest(num_top_nodes, 'edge_current_flow_betweenness_centrality')
plt.scatter(covid_edge_current_flow_betweenness_centrality['Node'], covid_edge_current_flow_betweenness_centrality['edge_current_flow_betweenness_centrality'], color='red')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Edge Current Flow Betweenness Centrality (COVID)')
plt.xticks(rotation=45)

# H1N1 Edge Betweenness Centrality
plt.subplot(2, 3, 4)
h1n1_edge_betweenness_centrality = h1n1_edge_betweenness_centrality.nlargest(num_top_nodes, 'edge_betweenness_centrality')
plt.scatter(h1n1_edge_betweenness_centrality['Node'], h1n1_edge_betweenness_centrality['edge_betweenness_centrality'], color='blue')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Edge Betweenness Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Edge Load Centrality
plt.subplot(2, 3, 5)
h1n1_edge_load_centrality = h1n1_edge_load_centrality.nlargest(num_top_nodes, 'edge_load_centrality')
plt.scatter(h1n1_edge_load_centrality['Node'], h1n1_edge_load_centrality['edge_load_centrality'], color='blue')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Edge Load Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Edge Current Flow Betweenness Centrality
plt.subplot(2, 3, 6)
h1n1_edge_current_flow_betweenness_centrality = h1n1_edge_current_flow_betweenness_centrality.nlargest(num_top_nodes, 'edge_current_flow_betweenness_centrality')
plt.scatter(h1n1_edge_current_flow_betweenness_centrality['Node'], h1n1_edge_current_flow_betweenness_centrality['edge_current_flow_betweenness_centrality'], color='blue')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Edge Current Flow Betweenness Centrality (H1N1)')
plt.xticks(rotation=45)

# Save the combined image
combined_filename = "figures/centrality_measures/7.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')

plt.tight_layout()
plt.show()