import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

file1_path = "datasets/corona_edges.csv"
file2_path = "datasets/influenza_edges.csv"
data1 = pd.read_csv(file1_path)
data2 = pd.read_csv(file2_path)

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


pos1 = nx.spring_layout(G1)
pos2 = nx.spring_layout(G2)

nx.draw(G1, pos1, ax=axes[0], with_labels=True, node_size=20, font_size=2)
nx.draw(G2, pos2, ax=axes[1], with_labels=True, node_size=20, font_size=2)


axes[0].set_title('Graph from corona_edges.csv')
axes[1].set_title('Graph from influenza_edges.csv')

combined_filename = "figures/visualisation_corona_influenza_datasets.png"
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')

plt.tight_layout()  
plt.show()