import networkx as nx

data1 = pd.read_excel("outputs/common_nodes/subgraph_edges_corona.xlsx")
data2 = pd.read_excel("outputs/common_nodes/subgraph_edges_influenza.xlsx")


subgraph1 = nx.Graph().to_undirected()
subgraph2 = nx.Graph().to_undirected()

for index, row in data1.iterrows():
    node1 = row["V1"]
    node2 = row["V2"]
    subgraph1.add_edge(node1, node2)

for index, row in data2.iterrows():
    node1 = row["V1"]
    node2 = row["V2"]
    subgraph2.add_edge(node1, node2)


node_degrees1 = dict(subgraph1.degree())
node_degrees2 = dict(subgraph2.degree())

# For reducing subgraph nodes
degree_threshold = 2 


nodes_to_keep_sub1 = [node for node, degree in node_degrees1.items() if degree > degree_threshold]
nodes_to_keep_sub2 = [node for node, degree in node_degrees2.items() if degree > degree_threshold]



fig, axes = plt.subplots(1, 2, figsize=(12, 6))  


reduced_subgraph1 = subgraph1.subgraph(nodes_to_keep_sub1)
reduced_subgraph2 = subgraph2.subgraph(nodes_to_keep_sub2)


pos1 = nx.spring_layout(reduced_subgraph1)
pos2 = nx.spring_layout(reduced_subgraph2)

nx.draw(reduced_subgraph1, pos1, ax=axes[0], with_labels=True, node_size=20, font_size=2)
nx.draw(reduced_subgraph2, pos2, ax=axes[1], with_labels=True, node_size=20, font_size=2)


axes[0].set_title('Subgraph SARS-CoV-2')
axes[1].set_title('Subgraph (H1N1) Influenza')

combined_graph = "figures/Reduced Subgraph 79 and 324 nodes.png"
plt.savefig(combined_graph, dpi=300, bbox_inches='tight')

plt.tight_layout()  
plt.show()

s1_nodes_df = pd.DataFrame(list(reduced_subgraph1.nodes()), columns=["reduced_nodes_corona"])
s1_edges_df = pd.DataFrame(list(reduced_subgraph1.edges()), columns=["V1", "V2"])
s2_nodes_df = pd.DataFrame(list(reduced_subgraph2.nodes()), columns=["reduced_nodes_influenza"])
s2_edges_df = pd.DataFrame(list(reduced_subgraph2.edges()), columns=["V1", "V2"])


s1_nodes_df.to_excel("outputs/common_nodes/reduced_graph/reduced_nodes_corona.xlsx", index=False)
s1_edges_df.to_excel("outputs/common_nodes/reduced_graph/reduced_edges_corona.xlsx", index=False)
s2_nodes_df.to_excel("outputs/common_nodes/reduced_graph/reduced_nodes_influenza.xlsx", index=False)
s2_edges_df.to_excel("outputs/common_nodes/reduced_graph/reduced_edges_influenza.xlsx", index=False)

print(reduced_subgraph1)
print(reduced_subgraph2)