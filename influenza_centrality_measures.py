import networkx as nx
import pandas as pd


influenza_edge_data = pd.read_csv("datasets/influenza_edges.csv"  )

G = nx.Graph().to_undirected()

edges = list(zip(influenza_edge_data["V1"], influenza_edge_data["V2"]))
G.add_edges_from(edges)


# Calculate centrality measures

closeness_centrality = nx.closeness_centrality(G)
harmonic_centrality = nx.harmonic_centrality(G)
eccentricity = nx.eccentricity(G)
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
subgraph_centrality = nx.subgraph_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G,max_iter=500 )
edge_betweenness_centrality=nx.edge_betweenness_centrality(G)
current_flow_closeness_centrality=nx.current_flow_closeness_centrality(G)
information_centrality=nx.information_centrality(G)
current_flow_betweenness_centrality=nx.current_flow_betweenness_centrality(G)
load_centrality=nx.load_centrality(G)
edge_load_centrality=nx.edge_load_centrality(G)
pagerank=nx.pagerank(G)
second_order_centrality=nx.second_order_centrality(G)
laplacian_centrality=nx.laplacian_centrality(G)
eigenvector_centrality_numpy=nx.eigenvector_centrality_numpy(G)
katz_centrality_numpy=nx.katz_centrality_numpy(G)
subgraph_centrality_exp=nx.subgraph_centrality_exp(G)
approximate_current_flow_betweenness_centrality=nx.approximate_current_flow_betweenness_centrality(G)
edge_current_flow_betweenness_centrality=nx.edge_current_flow_betweenness_centrality(G)
communicability_betweenness_centrality=nx.communicability_betweenness_centrality(G)
estrada_index = nx.estrada_index(G)
voterank=nx.voterank(G)
average_shortest_path_length=nx.average_shortest_path_length(G)
barycenter=nx.barycenter(G)
dispersion=nx.dispersion(G)


# Decay Centrality
delta = 0.5  # You can adjust this parameter as needed
decay_centrality = {}
for node in G.nodes:
    decay_values = [delta ** dist for dist in nx.shortest_path_length(G, source=node).values()]
    decay_centrality[node] = sum(decay_values)


# Radiality centrality
def calculate_radiality_centrality(graph):
    n = len(graph.nodes)
    diam = nx.diameter(graph)
    radiality_centrality = {}
    for u in graph.nodes:
        total_distance = 0
        for w in graph.nodes:
            if u != w:
                total_distance += (diam + 1 - nx.shortest_path_length(graph, source=u, target=w))
        radiality_centrality[u] = total_distance / (n - 1)
    return radiality_centrality

radiality_centrality = calculate_radiality_centrality(G)


# Store each centrality function in separate Excel files, sorted by centrality values

centrality_functions = {

    "closeness_centrality": closeness_centrality,
    "harmonic_centrality": harmonic_centrality,
    "eccentricity": eccentricity,
    "decay_centrality": decay_centrality,
    "subgraph_centrality": subgraph_centrality,
    "eigenvector_centrality": eigenvector_centrality,
    "degree_centrality": degree_centrality,
    "betweenness_centrality": betweenness_centrality,
    "edge_betweenness_centrality": edge_betweenness_centrality,
    "current_flow_closeness_centrality": current_flow_closeness_centrality,
    "information_centrality": information_centrality,
    "current_flow_betweenness_centrality": current_flow_betweenness_centrality,
    "load_centrality": load_centrality,
    "edge_load_centrality": edge_load_centrality,
    "pagerank": pagerank,
    "second_order_centrality": second_order_centrality,
    "laplacian_centrality":laplacian_centrality,
    "eigenvector_centrality_numpy": eigenvector_centrality_numpy,
    "katz_centrality_numpy": katz_centrality_numpy,
    "subgraph_centrality_exp": subgraph_centrality_exp,
    "approximate_current_flow_betweenness_centrality": approximate_current_flow_betweenness_centrality,
    "edge_current_flow_betweenness_centrality": edge_current_flow_betweenness_centrality,
    "communicability_betweenness_centrality": communicability_betweenness_centrality,
    "radiality_centrality":radiality_centrality,
}

for centrality_name, centrality_data in centrality_functions.items():
    sorted_data = sorted(centrality_data.items(), key=lambda x: x[1], reverse=True)
    df = pd.DataFrame(sorted_data, columns=["Node", centrality_name])
    excel_file_name = f"{centrality_name}.xlsx"
    excel_file_path = "outputs/influenza_centrality_measures/" + excel_file_name
    df.to_excel(excel_file_path, index=False)
    print(f"{centrality_name} data saved to {excel_file_name}")


# To print centrality measures or save in .txt file

print(estrada_index)
print(voterank)
print(average_shortest_path_length)
print(barycenter)
print(dispersion)

# We generated 3 centrality function from UCINet as follow 
# proximal_betweenness
# katz_centrality
# beta_beach_centrality