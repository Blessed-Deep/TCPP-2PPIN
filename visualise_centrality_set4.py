import pandas as pd
import matplotlib.pyplot as plt

# Load node labels for COVID and H1N1
covid_node_labels = pd.read_excel("datasets/corona_nodes.xlsx")
h1n1_node_labels = pd.read_excel("datasets/influenza_nodes.xlsx")

# Load centrality data for the two graphs and centrality measures
covid_eigenvector_centrality_numpy_data = pd.read_excel("outputs/corona_centrality_measures/eigenvector_centrality_numpy.xlsx")
h1n1_eigenvector_centrality_numpy_data = pd.read_excel("outputs/influenza_centrality_measures/eigenvector_centrality_numpy.xlsx")

covid_eccentricity_data = pd.read_excel("outputs/corona_centrality_measures/eccentricity.xlsx")
h1n1_eccentricity_data = pd.read_excel("outputs/influenza_centrality_measures/eccentricity.xlsx")

covid_decay_centrality_data = pd.read_excel("outputs/corona_centrality_measures/decay_centrality.xlsx")
h1n1_decay_centrality_data = pd.read_excel("outputs/influenza_centrality_measures/decay_centrality.xlsx")

covid_current_flow_closeness_centrality_data = pd.read_excel("outputs/corona_centrality_measures/current_flow_closeness_centrality.xlsx")
h1n1_current_flow_closeness_centrality_data = pd.read_excel("outputs/influenza_centrality_measures/current_flow_closeness_centrality.xlsx")

# Merge node labels with centrality data
covid_eigenvector_centrality_numpy_data = covid_eigenvector_centrality_numpy_data.merge(covid_node_labels, on='Node')
h1n1_eigenvector_centrality_numpy_data = h1n1_eigenvector_centrality_numpy_data.merge(h1n1_node_labels, on='Node')
covid_eccentricity_data = covid_eccentricity_data.merge(covid_node_labels, on='Node')
h1n1_eccentricity_data = h1n1_eccentricity_data.merge(h1n1_node_labels, on='Node')
covid_decay_centrality_data = covid_decay_centrality_data.merge(covid_node_labels, on='Node')
h1n1_decay_centrality_data = h1n1_decay_centrality_data.merge(h1n1_node_labels, on='Node')
covid_current_flow_closeness_centrality_data = covid_current_flow_closeness_centrality_data.merge(covid_node_labels, on='Node')
h1n1_current_flow_closeness_centrality_data = h1n1_current_flow_closeness_centrality_data.merge(h1n1_node_labels, on='Node')

# Choose the top number of nodes to visualize
num_top_nodes = 20

# Create subplots for each centrality measure
plt.figure(figsize=(25, 15))

# COVID Eigenvector Centrality Numpy
plt.subplot(2, 4, 1)
top_nodes_covid_eigenvector_centrality_numpy = covid_eigenvector_centrality_numpy_data.nlargest(num_top_nodes, 'eigenvector_centrality_numpy')
plt.scatter(top_nodes_covid_eigenvector_centrality_numpy['corona_nodes'], top_nodes_covid_eigenvector_centrality_numpy['eigenvector_centrality_numpy'], color='red')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Eigenvector Centrality Numpy (COVID)')
plt.xticks(rotation=45)

# COVID Eccentricity
plt.subplot(2, 4, 2)
top_nodes_covid_eccentricity = covid_eccentricity_data.nlargest(num_top_nodes, 'eccentricity')
plt.scatter(top_nodes_covid_eccentricity['corona_nodes'], top_nodes_covid_eccentricity['eccentricity'], color='green')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Eccentricity (COVID)')
plt.xticks(rotation=45)

# COVID Decay Centrality
plt.subplot(2, 4, 3)
top_nodes_covid_decay_centrality = covid_decay_centrality_data.nlargest(num_top_nodes, 'decay_centrality')
plt.scatter(top_nodes_covid_decay_centrality['corona_nodes'], top_nodes_covid_decay_centrality['decay_centrality'], color='blue')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Decay Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Current Flow Closeness Centrality
plt.subplot(2, 4, 4)
top_nodes_covid_current_flow_closeness_centrality = covid_current_flow_closeness_centrality_data.nlargest(num_top_nodes, 'current_flow_closeness_centrality')
plt.scatter(top_nodes_covid_current_flow_closeness_centrality['corona_nodes'], top_nodes_covid_current_flow_closeness_centrality['current_flow_closeness_centrality'], color='black')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Current Flow Closeness Centrality (COVID)')
plt.xticks(rotation=45)

# H1N1 Eigenvector Centrality Numpy
plt.subplot(2, 4, 5)
top_nodes_h1n1_eigenvector_centrality_numpy = h1n1_eigenvector_centrality_numpy_data.nlargest(num_top_nodes, 'eigenvector_centrality_numpy')
plt.scatter(top_nodes_h1n1_eigenvector_centrality_numpy['influenza_nodes'], top_nodes_h1n1_eigenvector_centrality_numpy['eigenvector_centrality_numpy'], color='purple')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Eigenvector Centrality Numpy (H1N1)')
plt.xticks(rotation=45)

# H1N1 Eccentricity
plt.subplot(2, 4, 6)
top_nodes_h1n1_eccentricity = h1n1_eccentricity_data.nlargest(num_top_nodes, 'eccentricity')
plt.scatter(top_nodes_h1n1_eccentricity['influenza_nodes'], top_nodes_h1n1_eccentricity['eccentricity'], color='brown')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Eccentricity (H1N1)')
plt.xticks(rotation=45)

# H1N1 Decay Centrality
plt.subplot(2, 4, 7)
top_nodes_h1n1_decay_centrality = h1n1_decay_centrality_data.nlargest(num_top_nodes, 'decay_centrality')
plt.scatter(top_nodes_h1n1_decay_centrality['influenza_nodes'], top_nodes_h1n1_decay_centrality['decay_centrality'], color='gray')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Decay Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Current Flow Closeness Centrality
plt.subplot(2, 4, 8)
top_nodes_h1n1_current_flow_closeness_centrality = h1n1_current_flow_closeness_centrality_data.nlargest(num_top_nodes, 'current_flow_closeness_centrality')
plt.scatter(top_nodes_h1n1_current_flow_closeness_centrality['influenza_nodes'], top_nodes_h1n1_current_flow_closeness_centrality['current_flow_closeness_centrality'], color='magenta')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Current Flow Closeness Centrality (H1N1)')
plt.xticks(rotation=45)

plt.tight_layout()

# Save the combined image
combined_filename = "figures/centrality_measures/4.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')
plt.show()