import pandas as pd
import matplotlib.pyplot as plt

# Load node labels for COVID and H1N1
covid_node_labels = pd.read_excel("datasets/corona_nodes.xlsx")
h1n1_node_labels = pd.read_excel("datasets/influenza_nodes.xlsx")

# Load centrality data for the two graphs and centrality measures
covid_current_flow_betweenness_data = pd.read_excel("outputs/corona_centrality_measures/current_flow_betweenness_centrality.xlsx")
h1n1_current_flow_betweenness_data = pd.read_excel("outputs/influenza_centrality_measures/current_flow_betweenness_centrality.xlsx")

covid_closeness_centrality_data = pd.read_excel("outputs/corona_centrality_measures/closeness_centrality.xlsx")
h1n1_closeness_centrality_data = pd.read_excel("outputs/influenza_centrality_measures/closeness_centrality.xlsx")

covid_betweenness_centrality_data = pd.read_excel("outputs/corona_centrality_measures/betweenness_centrality.xlsx")
h1n1_betweenness_centrality_data = pd.read_excel("outputs/influenza_centrality_measures/betweenness_centrality.xlsx")

covid_approximate_current_flow_betweenness_data = pd.read_excel("outputs/corona_centrality_measures/approximate_current_flow_betweenness_centrality.xlsx")
h1n1_approximate_current_flow_betweenness_data = pd.read_excel("outputs/influenza_centrality_measures/approximate_current_flow_betweenness_centrality.xlsx")

# Merge node labels with centrality data
covid_current_flow_betweenness_data = covid_current_flow_betweenness_data.merge(covid_node_labels, on='Node')
h1n1_current_flow_betweenness_data = h1n1_current_flow_betweenness_data.merge(h1n1_node_labels, on='Node')
covid_closeness_centrality_data = covid_closeness_centrality_data.merge(covid_node_labels, on='Node')
h1n1_closeness_centrality_data = h1n1_closeness_centrality_data.merge(h1n1_node_labels, on='Node')
covid_betweenness_centrality_data = covid_betweenness_centrality_data.merge(covid_node_labels, on='Node')
h1n1_betweenness_centrality_data = h1n1_betweenness_centrality_data.merge(h1n1_node_labels, on='Node')
covid_approximate_current_flow_betweenness_data = covid_approximate_current_flow_betweenness_data.merge(covid_node_labels, on='Node')
h1n1_approximate_current_flow_betweenness_data = h1n1_approximate_current_flow_betweenness_data.merge(h1n1_node_labels, on='Node')

# Choose the top number of nodes to visualize
num_top_nodes = 20

# Create subplots for each centrality measure
plt.figure(figsize=(25, 15))

# COVID Current Flow Betweenness Centrality
plt.subplot(2, 4, 1)
top_nodes_covid_current_flow_betweenness = covid_current_flow_betweenness_data.nlargest(num_top_nodes, 'current_flow_betweenness_centrality')
plt.scatter(top_nodes_covid_current_flow_betweenness['corona_nodes'], top_nodes_covid_current_flow_betweenness['current_flow_betweenness_centrality'], color='red')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Current Flow Betweenness Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Closeness Centrality
plt.subplot(2, 4, 2)
top_nodes_covid_closeness_centrality = covid_closeness_centrality_data.nlargest(num_top_nodes, 'closeness_centrality')
plt.scatter(top_nodes_covid_closeness_centrality['corona_nodes'], top_nodes_covid_closeness_centrality['closeness_centrality'], color='green')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Closeness Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Betweenness Centrality
plt.subplot(2, 4, 3)
top_nodes_covid_betweenness_centrality = covid_betweenness_centrality_data.nlargest(num_top_nodes, 'betweenness_centrality')
plt.scatter(top_nodes_covid_betweenness_centrality['corona_nodes'], top_nodes_covid_betweenness_centrality['betweenness_centrality'], color='blue')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Betweenness Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Approximate Current Flow Betweenness Centrality
plt.subplot(2, 4, 4)
top_nodes_covid_approximate_current_flow_betweenness = covid_approximate_current_flow_betweenness_data.nlargest(num_top_nodes, 'approximate_current_flow_betweenness_centrality')
plt.scatter(top_nodes_covid_approximate_current_flow_betweenness['corona_nodes'], top_nodes_covid_approximate_current_flow_betweenness['approximate_current_flow_betweenness_centrality'], color='black')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Approximate Current Flow Betweenness Centrality (COVID)')
plt.xticks(rotation=45)

# H1N1 Current Flow Betweenness Centrality
plt.subplot(2, 4, 5)
top_nodes_h1n1_current_flow_betweenness = h1n1_current_flow_betweenness_data.nlargest(num_top_nodes, 'current_flow_betweenness_centrality')
plt.scatter(top_nodes_h1n1_current_flow_betweenness['influenza_nodes'], top_nodes_h1n1_current_flow_betweenness['current_flow_betweenness_centrality'], color='purple')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Current Flow Betweenness Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Closeness Centrality
plt.subplot(2, 4, 6)
top_nodes_h1n1_closeness_centrality = h1n1_closeness_centrality_data.nlargest(num_top_nodes, 'closeness_centrality')
plt.scatter(top_nodes_h1n1_closeness_centrality['influenza_nodes'], top_nodes_h1n1_closeness_centrality['closeness_centrality'], color='brown')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Closeness Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Betweenness Centrality
plt.subplot(2, 4, 7)
top_nodes_h1n1_betweenness_centrality = h1n1_betweenness_centrality_data.nlargest(num_top_nodes, 'betweenness_centrality')
plt.scatter(top_nodes_h1n1_betweenness_centrality['influenza_nodes'], top_nodes_h1n1_betweenness_centrality['betweenness_centrality'], color='gray')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Betweenness Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Approximate Current Flow Betweenness Centrality
plt.subplot(2, 4, 8)
top_nodes_h1n1_approximate_current_flow_betweenness = h1n1_approximate_current_flow_betweenness_data.nlargest(num_top_nodes, 'approximate_current_flow_betweenness_centrality')
plt.scatter(top_nodes_h1n1_approximate_current_flow_betweenness['influenza_nodes'], top_nodes_h1n1_approximate_current_flow_betweenness['approximate_current_flow_betweenness_centrality'], color='magenta')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Approximate Current Flow Betweenness Centrality (H1N1)')
plt.xticks(rotation=45)

plt.tight_layout()

# Save the combined image
combined_filename = "figures/centrality_measures/5.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')
plt.show()