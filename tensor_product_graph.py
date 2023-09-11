import networkx as nx
import matplotlib.pyplot as plt

data1 = pd.read_excel("outputs/common_nodes/reduced_graph/reduced_edges_corona.xlsx")
data2 = pd.read_excel("outputs/common_nodes/reduced_graph/reduced_edges_influenza.xlsx")


reduced_subgraph1 = nx.Graph().to_undirected()
reduced_subgraph2 = nx.Graph().to_undirected()

for index, row in data1.iterrows():
    node1 = row["V1"]
    node2 = row["V2"]
    reduced_subgraph1.add_edge(node1, node2)

for index, row in data2.iterrows():
    node1 = row["V1"]
    node2 = row["V2"]
    reduced_subgraph2.add_edge(node1, node2)



tensor_product_graph = nx.tensor_product(reduced_subgraph1, reduced_subgraph2)

pos = nx.spring_layout(tensor_product_graph)


plt.figure(figsize=(40, 40))
nx.draw(tensor_product_graph, pos,  node_size=20)
plt.title('Tensor Product Graph',fontsize=55)

combined_graph = "figures/tensor product graph with reduced graphs.png"
plt.savefig(combined_graph, dpi=300, bbox_inches='tight')

plt.show()

tpg_nodes_data = [{'Node': node} for node in tensor_product_graph.nodes()]
nodes_df = pd.DataFrame(tpg_nodes_data)
  
tpg_edges_data = [{'Source': source, 'Target': target} for source, target in tensor_product_graph.edges()]
edges_df = pd.DataFrame(tpg_edges_data)

nodes_df.to_csv('outputs/tensor_product_nodes.csv', index=False)
edges_df.to_csv('outputs/tensor_product_edges.csv', index=False)
