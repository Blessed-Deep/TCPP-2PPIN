from textwrap import indent
import pandas as pd

file_path_all_nodes = "outputs/influenza_centrality_measures/influenza_data_for_analysis/influenza_centrality_data.xlsx"

# file_path_filtered_nodes = "common_nodes/reduced_graph/subgraph_nodes_influenza.xlsx"
file_path_filtered_nodes = "outputs/common_nodes/reduced_graph/reduced_nodes_influenza.xlsx"

all_nodes_df = pd.read_excel(file_path_all_nodes)

filtered_nodes_df = pd.read_excel(file_path_filtered_nodes)

filtered_node_list = filtered_nodes_df['reduced_nodes_influenza'].tolist()


#H1N1 top 10 measures from PCA
desired_centrality_measures = [
    'eigenvector_centrality',
    'eigenvector_centrality_numpy',
    'katz_centrality',
    'communicability_betweenness_centrality',
    'degree_centrality',
    'laplacian_centrality',
    'betweenness_centrality',
    'current_flow_betweenness_centrality',
    'load_centrality',
    'pagerank',
]

# Filter the rows in the all_nodes_df based on the nodes in filtered_node_list
filtered_df = all_nodes_df[all_nodes_df['influenza_nodes'].isin(filtered_node_list)] 

# Select the desired centrality measures columns
desired_columns = ['influenza_nodes'] + desired_centrality_measures
filtered_df = filtered_df[desired_columns]


# Calculate the average of the 10 centrality measures and add a new "average" column
filtered_df['average'] = filtered_df[desired_centrality_measures].mean(axis=1)
print(filtered_df)

# Find the node with the highest average
node_with_highest_average = filtered_df.loc[filtered_df['average'].idxmax()]


print("Node with Highest Average:")
print(node_with_highest_average)
