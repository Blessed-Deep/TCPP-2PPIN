import pandas as pd
import matplotlib.pyplot as plt

# Load node labels for COVID and H1N1
covid_node_labels = pd.read_excel("datasets/corona_nodes.xlsx")
h1n1_node_labels = pd.read_excel("datasets/influenza_nodes.xlsx")

# Load centrality data for the two graphs and centrality measures
covid_degree_data = pd.read_excel("outputs/corona_centrality_measures/degree_centrality.xlsx")
h1n1_degree_data = pd.read_excel("outputs/influenza_centrality_measures/degree_centrality.xlsx")

covid_subgraph_data = pd.read_excel("outputs/corona_centrality_measures/subgraph_centrality.xlsx")
h1n1_subgraph_data = pd.read_excel("outputs/influenza_centrality_measures/subgraph_centrality.xlsx")

covid_subgraph_exp_data = pd.read_excel("outputs/corona_centrality_measures/subgraph_centrality_exp.xlsx")
h1n1_subgraph_exp_data = pd.read_excel("outputs/influenza_centrality_measures/subgraph_centrality_exp.xlsx")

covid_second_order_data = pd.read_excel("outputs/corona_centrality_measures/second_order_centrality.xlsx")
h1n1_second_order_data = pd.read_excel("outputs/influenza_centrality_measures/second_order_centrality.xlsx")

# Merge node labels with centrality data
covid_degree_data = covid_degree_data.merge(covid_node_labels, on='Node')
h1n1_degree_data = h1n1_degree_data.merge(h1n1_node_labels, on='Node')
covid_subgraph_data = covid_subgraph_data.merge(covid_node_labels, on='Node')
h1n1_subgraph_data = h1n1_subgraph_data.merge(h1n1_node_labels, on='Node')
covid_subgraph_exp_data = covid_subgraph_exp_data.merge(covid_node_labels, on='Node')
h1n1_subgraph_exp_data = h1n1_subgraph_exp_data.merge(h1n1_node_labels, on='Node')
covid_second_order_data = covid_second_order_data.merge(covid_node_labels, on='Node')
h1n1_second_order_data = h1n1_second_order_data.merge(h1n1_node_labels, on='Node')

# Choose the top number of nodes to visualize
num_top_nodes = 20

# Create subplots for each centrality measure
plt.figure(figsize=(25, 15))

# COVID Degree Centrality
plt.subplot(2, 4, 1)
top_nodes_covid_degree = covid_degree_data.nlargest(num_top_nodes, 'degree_centrality')
plt.scatter(top_nodes_covid_degree['corona_nodes'], top_nodes_covid_degree['degree_centrality'], color='red')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Degree Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Subgraph Centrality
plt.subplot(2, 4, 2)
top_nodes_covid_subgraph = covid_subgraph_data.nlargest(num_top_nodes, 'subgraph_centrality')
plt.scatter(top_nodes_covid_subgraph['corona_nodes'], top_nodes_covid_subgraph['subgraph_centrality'], color='green')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Subgraph Centrality (COVID)')
plt.xticks(rotation=45)

# COVID Subgraph Centrality Exp
plt.subplot(2, 4, 3)
top_nodes_covid_subgraph_exp = covid_subgraph_exp_data.nlargest(num_top_nodes, 'subgraph_centrality_exp')
plt.scatter(top_nodes_covid_subgraph_exp['corona_nodes'], top_nodes_covid_subgraph_exp['subgraph_centrality_exp'], color='blue')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Subgraph Centrality Exp (COVID)')
plt.xticks(rotation=45)

# COVID Second Order Centrality
plt.subplot(2, 4, 4)
top_nodes_covid_second_order = covid_second_order_data.nlargest(num_top_nodes, 'second_order_centrality')
plt.scatter(top_nodes_covid_second_order['corona_nodes'], top_nodes_covid_second_order['second_order_centrality'], color='black')
plt.xlabel('SARS-CoV-2')
plt.ylabel('Centrality Value')
plt.title('Second Order Centrality (COVID)')
plt.xticks(rotation=45)

# H1N1 Degree Centrality
plt.subplot(2, 4, 5)
top_nodes_h1n1_degree = h1n1_degree_data.nlargest(num_top_nodes, 'degree_centrality')
plt.scatter(top_nodes_h1n1_degree['influenza_nodes'], top_nodes_h1n1_degree['degree_centrality'], color='purple')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title('Degree Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Subgraph Centrality
plt.subplot(2, 4, 6)
top_nodes_h1n1_subgraph = h1n1_subgraph_data.nlargest(num_top_nodes, 'subgraph_centrality')
plt.scatter(top_nodes_h1n1_subgraph['influenza_nodes'], top_nodes_h1n1_subgraph['subgraph_centrality'], color='brown')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title('Subgraph Centrality (H1N1)')
plt.xticks(rotation=45)

# H1N1 Subgraph Centrality Exp
plt.subplot(2, 4, 7)
top_nodes_h1n1_subgraph_exp = h1n1_subgraph_exp_data.nlargest(num_top_nodes, 'subgraph_centrality_exp')
plt.scatter(top_nodes_h1n1_subgraph_exp['influenza_nodes'], top_nodes_h1n1_subgraph_exp['subgraph_centrality_exp'], color='gray')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title('Subgraph Centrality Exp (H1N1)')
plt.xticks(rotation=45)

# H1N1 Second Order Centrality
plt.subplot(2, 4, 8)
top_nodes_h1n1_second_order = h1n1_second_order_data.nlargest(num_top_nodes, 'second_order_centrality')
plt.scatter(top_nodes_h1n1_second_order['influenza_nodes'], top_nodes_h1n1_second_order['second_order_centrality'], color='magenta')
plt.xlabel('(H1N1) Influenza')
plt.ylabel('Centrality Value')
plt.title('Second Order Centrality (H1N1)')
plt.xticks(rotation=45)

plt.tight_layout()

# Save the combined image
combined_filename = "figures/centrality_measures/1.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')
plt.show()