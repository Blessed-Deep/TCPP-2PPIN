import pandas as pd
import matplotlib.pyplot as plt

# Load node labels for COVID and H1N1
covid_node_labels = pd.read_excel("datasets/corona_nodes.xlsx")
h1n1_node_labels = pd.read_excel("datasets/influenza_nodes.xlsx")

# Load centrality data for the two graphs and centrality measures
covid_proximal_betweenness_data = pd.read_excel("outputs/corona_centrality_measures/proximal_betweenness.xlsx")
h1n1_proximal_betweenness_data = pd.read_excel("outputs/influenza_centrality_measures/proximal_betweenness.xlsx")

covid_katz_centrality_data = pd.read_excel("outputs/corona_centrality_measures/katz_centrality.xlsx")
h1n1_katz_centrality_data = pd.read_excel("outputs/influenza_centrality_measures/katz_centrality.xlsx")

covid_beta_reach_centrality_data = pd.read_excel("outputs/corona_centrality_measures/beta_reach_centrality.xlsx")
h1n1_beta_reach_centrality_data = pd.read_excel("outputs/influenza_centrality_measures/beta_reach_centrality.xlsx")

covid_communicability_betweenness_data = pd.read_excel("outputs/corona_centrality_measures/communicability_betweenness_centrality.xlsx")
h1n1_communicability_betweenness_data = pd.read_excel("outputs/influenza_centrality_measures/communicability_betweenness_centrality.xlsx")

# Merge node labels with centrality data
covid_proximal_betweenness_data = covid_proximal_betweenness_data.merge(covid_node_labels, on='Node')
h1n1_proximal_betweenness_data = h1n1_proximal_betweenness_data.merge(h1n1_node_labels, on='Node')
covid_katz_centrality_data = covid_katz_centrality_data.merge(covid_node_labels, on='Node')
h1n1_katz_centrality_data = h1n1_katz_centrality_data.merge(h1n1_node_labels, on='Node')
covid_beta_reach_centrality_data = covid_beta_reach_centrality_data.merge(covid_node_labels, on='Node')
h1n1_beta_reach_centrality_data = h1n1_beta_reach_centrality_data.merge(h1n1_node_labels, on='Node')
covid_communicability_betweenness_data = covid_communicability_betweenness_data.merge(covid_node_labels, on='Node')
h1n1_communicability_betweenness_data = h1n1_communicability_betweenness_data.merge(h1n1_node_labels, on='Node')

# Choose the top number of nodes to visualize
num_top_nodes = 20

# Create subplots for each centrality measure
plt.figure(figsize=(25, 15))

# COVID Proximal Betweenness Centrality
plt.subplot(2, 4, 1)
top_nodes_covid_proximal_betweenness = covid_proximal_betweenness_data.nlargest(num_top_nodes, 'proximal_betweenness')
plt.scatter(top_nodes_covid_proximal_betweenness['corona_nodes'], top_nodes_covid_proximal_betweenness['proximal_betweenness'], color='red')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Proximal Betweenness Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Katz Centrality
plt.subplot(2, 4, 2)
top_nodes_covid_katz_centrality = covid_katz_centrality_data.nlargest(num_top_nodes, 'katz_centrality')
plt.scatter(top_nodes_covid_katz_centrality['corona_nodes'], top_nodes_covid_katz_centrality['katz_centrality'], color='green')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Katz Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Beta Reach Centrality
plt.subplot(2, 4, 3)
top_nodes_covid_beta_reach_centrality = covid_beta_reach_centrality_data.nlargest(num_top_nodes, 'beta_reach_centrality')
plt.scatter(top_nodes_covid_beta_reach_centrality['corona_nodes'], top_nodes_covid_beta_reach_centrality['beta_reach_centrality'], color='blue')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Beta Reach Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Communicability Betweenness Centrality
plt.subplot(2, 4, 4)
top_nodes_covid_communicability_betweenness = covid_communicability_betweenness_data.nlargest(num_top_nodes, 'communicability_betweenness_centrality')
plt.scatter(top_nodes_covid_communicability_betweenness['corona_nodes'], top_nodes_covid_communicability_betweenness['communicability_betweenness_centrality'], color='black')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Communicability Betweenness Centrality (COVID)')
plt.xticks(rotation=45)

# H1N1 Proximal Betweenness Centrality
plt.subplot(2, 4, 5)
top_nodes_h1n1_proximal_betweenness = h1n1_proximal_betweenness_data.nlargest(num_top_nodes, 'proximal_betweenness')
plt.scatter(top_nodes_h1n1_proximal_betweenness['influenza_nodes'], top_nodes_h1n1_proximal_betweenness['proximal_betweenness'], color='purple')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Proximal Betweenness Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Katz Centrality
plt.subplot(2, 4, 6)
top_nodes_h1n1_katz_centrality = h1n1_katz_centrality_data.nlargest(num_top_nodes, 'katz_centrality')
plt.scatter(top_nodes_h1n1_katz_centrality['influenza_nodes'], top_nodes_h1n1_katz_centrality['katz_centrality'], color='brown')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Katz Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Beta Reach Centrality
plt.subplot(2, 4, 7)
top_nodes_h1n1_beta_reach_centrality = h1n1_beta_reach_centrality_data.nlargest(num_top_nodes, 'beta_reach_centrality')
plt.scatter(top_nodes_h1n1_beta_reach_centrality['influenza_nodes'], top_nodes_h1n1_beta_reach_centrality['beta_reach_centrality'], color='gray')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Beta Reach Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Communicability Betweenness Centrality
plt.subplot(2, 4, 8)
top_nodes_h1n1_communicability_betweenness = h1n1_communicability_betweenness_data.nlargest(num_top_nodes, 'communicability_betweenness_centrality')
plt.scatter(top_nodes_h1n1_communicability_betweenness['influenza_nodes'], top_nodes_h1n1_communicability_betweenness['communicability_betweenness_centrality'], color='magenta')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Communicability Betweenness Centrality (H1N1)')
plt.xticks(rotation=45)

plt.tight_layout()

# Save the combined image
combined_filename = "figures/centrality_measures/6.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')
plt.show()