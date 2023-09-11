# root node -----> ('P0DTD8', 'P03470') 

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

nodes_csv = 'outputs/tensor_product_nodes.csv'
edges_csv = 'outputs/tensor_product_edges.csv'

nodes_df = pd.read_csv(nodes_csv)
edges_df = pd.read_csv(edges_csv)

tpg = nx.Graph()


for _, row in nodes_df.iterrows():
    node = row['Node']
    tpg.add_node(node)

for _, row in edges_df.iterrows():
    source = row['Source']
    target = row['Target']
    tpg.add_edge(source, target)
    

root_node = '(\'P0DTD8\', \'P03470\')'

neighbors = list(tpg.neighbors(root_node))

tpg_subgraph = tpg.subgraph([root_node] + neighbors)

pos = nx.spring_layout(tpg_subgraph)


plt.figure(figsize=(20, 20))
nx.draw(tpg_subgraph, pos,  node_size=20)

combined_graph = "figures/3744 immediate neighbors from the root_node.png"
plt.savefig(combined_graph, dpi=300, bbox_inches='tight')


plt.show()