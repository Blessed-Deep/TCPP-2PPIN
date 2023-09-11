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

common_nodes_list = []

for index, row in common_nodes.iterrows():
    node = row["common_nodes_list"]
    common_nodes_list.append(node)


fig, axes = plt.subplots(1, 2, figsize=(12, 6))  


c_list = common_nodes_list # Fill in your list of common nodes here default is #1f78b4


node_colors_g1 = ['red' if node in c_list else 'blue' for node in G1.nodes()]
node_colors_g2 = ['red' if node in c_list else 'blue' for node in G2.nodes()]
    

pos1 = nx.spring_layout(G1)
pos2 = nx.spring_layout(G2)

nx.draw(G1, pos1, ax=axes[0], with_labels=True, node_size=20, font_size=2, node_color=node_colors_g1)
nx.draw(G2, pos2, ax=axes[1], with_labels=True, node_size=20, font_size=2, node_color=node_colors_g2)


axes[0].set_title('Common nodes SARS-CoV-2')
axes[1].set_title('Common nodes (H1N1) Influenza')

combined_graph = "figures/common_nodes_corona_influenza_dataset.png"
plt.savefig(combined_graph, dpi=300, bbox_inches='tight')


plt.tight_layout()
plt.show()