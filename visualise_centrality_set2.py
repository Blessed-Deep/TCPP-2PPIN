import pandas as pd
import matplotlib.pyplot as plt

# Load node labels for COVID and H1N1
covid_node_labels = pd.read_excel("datasets/corona_nodes.xlsx")
h1n1_node_labels = pd.read_excel("datasets/influenza_nodes.xlsx")

# Load centrality data for the two graphs and centrality measures
covid_radiality_data = pd.read_excel("outputs/corona_centrality_measures/radiality_centrality.xlsx")
h1n1_radiality_data = pd.read_excel("outputs/influenza_centrality_measures/radiality_centrality.xlsx")

covid_pagerank_data = pd.read_excel("outputs/corona_centrality_measures/pagerank.xlsx")
h1n1_pagerank_data = pd.read_excel("outputs/influenza_centrality_measures/pagerank.xlsx")

covid_load_centrality_data = pd.read_excel("outputs/corona_centrality_measures/load_centrality.xlsx")
h1n1_load_centrality_data = pd.read_excel("outputs/influenza_centrality_measures/load_centrality.xlsx")

covid_laplacian_centrality_data = pd.read_excel("outputs/corona_centrality_measures/laplacian_centrality.xlsx")
h1n1_laplacian_centrality_data = pd.read_excel("outputs/influenza_centrality_measures/laplacian_centrality.xlsx")

# Merge node labels with centrality data
covid_radiality_data = covid_radiality_data.merge(covid_node_labels, on='Node')
h1n1_radiality_data = h1n1_radiality_data.merge(h1n1_node_labels, on='Node')
covid_pagerank_data = covid_pagerank_data.merge(covid_node_labels, on='Node')
h1n1_pagerank_data = h1n1_pagerank_data.merge(h1n1_node_labels, on='Node')
covid_load_centrality_data = covid_load_centrality_data.merge(covid_node_labels, on='Node')
h1n1_load_centrality_data = h1n1_load_centrality_data.merge(h1n1_node_labels, on='Node')
covid_laplacian_centrality_data = covid_laplacian_centrality_data.merge(covid_node_labels, on='Node')
h1n1_laplacian_centrality_data = h1n1_laplacian_centrality_data.merge(h1n1_node_labels, on='Node')

# Choose the top number of nodes to visualize
num_top_nodes = 20

# Create subplots for each centrality measure
plt.figure(figsize=(25, 15))

# COVID Radiality Centrality
plt.subplot(2, 4, 1)
top_nodes_covid_radiality = covid_radiality_data.nlargest(num_top_nodes, 'radiality_centrality')
plt.scatter(top_nodes_covid_radiality['corona_nodes'], top_nodes_covid_radiality['radiality_centrality'], color='red')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Radiality Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Pagerank Centrality
plt.subplot(2, 4, 2)
top_nodes_covid_pagerank = covid_pagerank_data.nlargest(num_top_nodes, 'pagerank')
plt.scatter(top_nodes_covid_pagerank['corona_nodes'], top_nodes_covid_pagerank['pagerank'], color='green')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Pagerank Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Load Centrality
plt.subplot(2, 4, 3)
top_nodes_covid_load_centrality = covid_load_centrality_data.nlargest(num_top_nodes, 'load_centrality')
plt.scatter(top_nodes_covid_load_centrality['corona_nodes'], top_nodes_covid_load_centrality['load_centrality'], color='blue')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Load Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Laplacian Centrality
plt.subplot(2, 4, 4)
top_nodes_covid_laplacian_centrality = covid_laplacian_centrality_data.nlargest(num_top_nodes, 'laplacian_centrality')
plt.scatter(top_nodes_covid_laplacian_centrality['corona_nodes'], top_nodes_covid_laplacian_centrality['laplacian_centrality'], color='black')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Laplacian Centrality (COVID)')
plt.xticks(rotation=45)

# H1N1 Radiality Centrality
plt.subplot(2, 4, 5)
top_nodes_h1n1_radiality = h1n1_radiality_data.nlargest(num_top_nodes, 'radiality_centrality')
plt.scatter(top_nodes_h1n1_radiality['influenza_nodes'], top_nodes_h1n1_radiality['radiality_centrality'], color='purple')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Radiality Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Pagerank Centrality
plt.subplot(2, 4, 6)
top_nodes_h1n1_pagerank = h1n1_pagerank_data.nlargest(num_top_nodes, 'pagerank')
plt.scatter(top_nodes_h1n1_pagerank['influenza_nodes'], top_nodes_h1n1_pagerank['pagerank'], color='brown')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Pagerank Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Load Centrality
plt.subplot(2, 4, 7)
top_nodes_h1n1_load_centrality = h1n1_load_centrality_data.nlargest(num_top_nodes, 'load_centrality')
plt.scatter(top_nodes_h1n1_load_centrality['influenza_nodes'], top_nodes_h1n1_load_centrality['load_centrality'], color='gray')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Load Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Laplacian Centrality
plt.subplot(2, 4, 8)
top_nodes_h1n1_laplacian_centrality = h1n1_laplacian_centrality_data.nlargest(num_top_nodes, 'laplacian_centrality')
plt.scatter(top_nodes_h1n1_laplacian_centrality['influenza_nodes'], top_nodes_h1n1_laplacian_centrality['laplacian_centrality'], color='magenta')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Laplacian Centrality (H1N1)')
plt.xticks(rotation=45)

plt.tight_layout()


# Save the combined image
combined_filename = "figures/centrality_measures/2.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')
plt.show()