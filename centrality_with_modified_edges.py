import networkx as nx
import pandas as pd

corona_edge_data = pd.read_excel("datasets/corona_edges_modified.xlsx"  )
influenza_edge_data = pd.read_excel("datasets/influenza_edges_modified.xlsx"  )

C = nx.Graph().to_undirected()
I = nx.Graph().to_undirected()

c_edges = list(zip(corona_edge_data["V1"], corona_edge_data["V2"]))
C.add_edges_from(c_edges)
i_edges = list(zip(influenza_edge_data["V1"], influenza_edge_data["V2"]))
I.add_edges_from(i_edges)


# Calculate centrality measures

c_edge_betweenness_centrality=nx.edge_betweenness_centrality(C)
c_edge_load_centrality=nx.edge_load_centrality(C)
c_edge_current_flow_betweenness_centrality=nx.edge_current_flow_betweenness_centrality(C)

i_edge_betweenness_centrality=nx.edge_betweenness_centrality(I)
i_edge_load_centrality=nx.edge_load_centrality(I)
i_edge_current_flow_betweenness_centrality=nx.edge_current_flow_betweenness_centrality(I)



# Store each centrality function in separate Excel files, sorted by centrality values

c_centrality_functions = {
    "edge_betweenness_centrality_modified": c_edge_betweenness_centrality,
    "edge_load_centrality_modified": c_edge_load_centrality,
    "edge_current_flow_betweenness_centrality_modified": c_edge_current_flow_betweenness_centrality
}

i_centrality_functions = {
    "edge_betweenness_centrality_modified": i_edge_betweenness_centrality,
    "edge_load_centrality_modified": i_edge_load_centrality,
    "edge_current_flow_betweenness_centrality_modified": i_edge_current_flow_betweenness_centrality
}

for centrality_name, centrality_data in c_centrality_functions.items():
    sorted_data = sorted(centrality_data.items(), key=lambda x: x[1], reverse=True)
    df = pd.DataFrame(sorted_data, columns=["Node", centrality_name])
    excel_file_name = f"{centrality_name}.xlsx"
    excel_file_path = "outputs/corona_centrality_measures/modified/" + excel_file_name
    df.to_excel(excel_file_path, index=False)
    print(f"{centrality_name} data saved to {excel_file_name}")

for centrality_name, centrality_data in i_centrality_functions.items():
    sorted_data = sorted(centrality_data.items(), key=lambda x: x[1], reverse=True)
    df = pd.DataFrame(sorted_data, columns=["Node", centrality_name])
    excel_file_name = f"{centrality_name}.xlsx"
    excel_file_path = "outputs/influenza_centrality_measures/modified/" + excel_file_name
    df.to_excel(excel_file_path, index=False)
    print(f"{centrality_name} data saved to {excel_file_name}")
