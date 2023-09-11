import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt



data1 = pd.read_excel("datasets/corona_edges_modified.xlsx")
data2 = pd.read_excel("datasets/influenza_edges_modified.xlsx")
common_nodes = pd.read_excel("outputs/common_nodes/common_nodes_list.xlsx")

G1 = nx.Graph().to_undirected()
G2 = nx.Graph().to_undirected()

for index, row in data1.iterrows():
    node1 = row["V1"]
    node2 = row["V2"]
    G1.add_edge(node1, node2)

for index, row in data2.iterrows():
    node1 = row["V1"]
    node2 = row["V2"]
    G2.add_edge(node1, node2)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))  

common_nodes_list = []

for index, row in common_nodes.iterrows():
    node = row["common_nodes_list"]
    common_nodes_list.append(node)



c_list = common_nodes_list # Fill in your list of common nodes here default is #1f78b4


subgraph1 = nx.Graph()
subgraph2 = nx.Graph()


subgraph1.add_nodes_from(c_list)
subgraph2.add_nodes_from(c_list)


for node in c_list:
    neighbors = list(G1.neighbors(node))
    subgraph1.add_nodes_from(neighbors)
    subgraph1.add_edges_from((node, neighbor) for neighbor in neighbors)
for node in c_list:
    neighbors = list(G2.neighbors(node))
    subgraph2.add_nodes_from(neighbors)
    subgraph2.add_edges_from((node, neighbor) for neighbor in neighbors)

node_colors_subg1 = ['red' if node in c_list else 'blue' for node in subgraph1.nodes()]
node_colors_subg2 = ['red' if node in c_list else 'blue' for node in subgraph2.nodes()]
    


pos1 = nx.spring_layout(subgraph1)
pos2 = nx.spring_layout(subgraph2)

nx.draw(subgraph1, pos1, ax=axes[0], with_labels=True, node_size=20, font_size=2, node_color=node_colors_subg1)
nx.draw(subgraph2, pos2, ax=axes[1], with_labels=True, node_size=20, font_size=2, node_color=node_colors_subg2)


axes[0].set_title('Common nodes SARS-CoV-2')
axes[1].set_title('Common nodes (H1N1) Influenza')

combined_graph = "figures/subgraph_common_nodes_corona_influenza_dataset.png"
plt.savefig(combined_graph, dpi=300, bbox_inches='tight')

plt.tight_layout() 
plt.show()

s1_nodes_df = pd.DataFrame(list(subgraph1.nodes()), columns=["sub_nodes_corona"])
s1_edges_df = pd.DataFrame(list(subgraph1.edges()), columns=["V1", "V2"])
s2_nodes_df = pd.DataFrame(list(subgraph2.nodes()), columns=["sub_nodes_influenza"])
s2_edges_df = pd.DataFrame(list(subgraph2.edges()), columns=["V1", "V2"])

# Save nodes and edges dataframes to Excel files
s1_nodes_df.to_excel("outputs/common_nodes/subgraph_nodes_corona.xlsx", index=False)
s1_edges_df.to_excel("outputs/common_nodes/subgraph_edges_corona.xlsx", index=False)
s2_nodes_df.to_excel("outputs/common_nodes/subgraph_nodes_influenza.xlsx", index=False)
s2_edges_df.to_excel("outputs/common_nodes/subgraph_edges_influenza.xlsx", index=False)
