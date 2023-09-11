import pandas as pd
import matplotlib.pyplot as plt

# Load node labels for COVID and H1N1
covid_node_labels = pd.read_excel("datasets/corona_nodes.xlsx")
h1n1_node_labels = pd.read_excel("datasets/influenza_nodes.xlsx")

# Load centrality data for the two graphs and centrality measures
covid_katz_centrality_data = pd.read_excel("outputs/corona_centrality_measures/katz_centrality_numpy.xlsx")
h1n1_katz_centrality_data = pd.read_excel("outputs/influenza_centrality_measures/katz_centrality_numpy.xlsx")

covid_information_centrality_data = pd.read_excel("outputs/corona_centrality_measures/information_centrality.xlsx")
h1n1_information_centrality_data = pd.read_excel("outputs/influenza_centrality_measures/information_centrality.xlsx")

covid_harmonic_centrality_data = pd.read_excel("outputs/corona_centrality_measures/harmonic_centrality.xlsx")
h1n1_harmonic_centrality_data = pd.read_excel("outputs/influenza_centrality_measures/harmonic_centrality.xlsx")

covid_eigenvector_centrality_data = pd.read_excel("outputs/corona_centrality_measures/eigenvector_centrality.xlsx")
h1n1_eigenvector_centrality_data = pd.read_excel("outputs/influenza_centrality_measures/eigenvector_centrality.xlsx")

# Merge node labels with centrality data
covid_katz_centrality_data = covid_katz_centrality_data.merge(covid_node_labels, on='Node')
h1n1_katz_centrality_data = h1n1_katz_centrality_data.merge(h1n1_node_labels, on='Node')
covid_information_centrality_data = covid_information_centrality_data.merge(covid_node_labels, on='Node')
h1n1_information_centrality_data = h1n1_information_centrality_data.merge(h1n1_node_labels, on='Node')
covid_harmonic_centrality_data = covid_harmonic_centrality_data.merge(covid_node_labels, on='Node')
h1n1_harmonic_centrality_data = h1n1_harmonic_centrality_data.merge(h1n1_node_labels, on='Node')
covid_eigenvector_centrality_data = covid_eigenvector_centrality_data.merge(covid_node_labels, on='Node')
h1n1_eigenvector_centrality_data = h1n1_eigenvector_centrality_data.merge(h1n1_node_labels, on='Node')

# Choose the top number of nodes to visualize
num_top_nodes = 20

# Create subplots for each centrality measure
plt.figure(figsize=(25, 15))

# COVID Katz Centrality Numpy
plt.subplot(2, 4, 1)
top_nodes_covid_katz_centrality = covid_katz_centrality_data.nlargest(num_top_nodes, 'katz_centrality_numpy')
plt.scatter(top_nodes_covid_katz_centrality['corona_nodes'], top_nodes_covid_katz_centrality['katz_centrality_numpy'], color='red')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Katz Centrality Numpy (COVID)')
plt.xticks(rotation=45)

# COVID Information Centrality
plt.subplot(2, 4, 2)
top_nodes_covid_information_centrality = covid_information_centrality_data.nlargest(num_top_nodes, 'information_centrality')
plt.scatter(top_nodes_covid_information_centrality['corona_nodes'], top_nodes_covid_information_centrality['information_centrality'], color='green')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Information Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Harmonic Centrality
plt.subplot(2, 4, 3)
top_nodes_covid_harmonic_centrality = covid_harmonic_centrality_data.nlargest(num_top_nodes, 'harmonic_centrality')
plt.scatter(top_nodes_covid_harmonic_centrality['corona_nodes'], top_nodes_covid_harmonic_centrality['harmonic_centrality'], color='blue')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Harmonic Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Eigenvector Centrality
plt.subplot(2, 4, 4)
top_nodes_covid_eigenvector_centrality = covid_eigenvector_centrality_data.nlargest(num_top_nodes, 'eigenvector_centrality')
plt.scatter(top_nodes_covid_eigenvector_centrality['corona_nodes'], top_nodes_covid_eigenvector_centrality['eigenvector_centrality'], color='black')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title(' Eigenvector Centrality (COVID)')
plt.xticks(rotation=45)

# H1N1 Katz Centrality Numpy
plt.subplot(2, 4, 5)
top_nodes_h1n1_katz_centrality = h1n1_katz_centrality_data.nlargest(num_top_nodes, 'katz_centrality_numpy')
plt.scatter(top_nodes_h1n1_katz_centrality['influenza_nodes'], top_nodes_h1n1_katz_centrality['katz_centrality_numpy'], color='purple')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Katz Centrality Numpy (H1N1)')
plt.xticks(rotation=45)

# H1N1 Information Centrality
plt.subplot(2, 4, 6)
top_nodes_h1n1_information_centrality = h1n1_information_centrality_data.nlargest(num_top_nodes, 'information_centrality')
plt.scatter(top_nodes_h1n1_information_centrality['influenza_nodes'], top_nodes_h1n1_information_centrality['information_centrality'], color='brown')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Information Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Harmonic Centrality
plt.subplot(2, 4, 7)
top_nodes_h1n1_harmonic_centrality = h1n1_harmonic_centrality_data.nlargest(num_top_nodes, 'harmonic_centrality')
plt.scatter(top_nodes_h1n1_harmonic_centrality['influenza_nodes'], top_nodes_h1n1_harmonic_centrality['harmonic_centrality'], color='gray')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Harmonic Centrality  (H1N1)')
plt.xticks(rotation=45)

# H1N1 Eigenvector Centrality
plt.subplot(2, 4, 8)
top_nodes_h1n1_eigenvector_centrality = h1n1_eigenvector_centrality_data.nlargest(num_top_nodes, 'eigenvector_centrality')
plt.scatter(top_nodes_h1n1_eigenvector_centrality['influenza_nodes'], top_nodes_h1n1_eigenvector_centrality['eigenvector_centrality'], color='magenta')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title(' Eigenvector Centrality (H1N1)')
plt.xticks(rotation=45)

plt.tight_layout()


# Save the combined image
combined_filename = "figures/centrality_measures/3.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')
plt.show()