import networkx as nx
import pandas as pd

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





rootlevel_corona_nodes = pd.read_excel("outputs/rootlevel_corona_nodes.xlsx")

c_level1 = []
c_level2 = []
c_level3 = []
c_level4 = []
c_level5 = []

for index, level in rootlevel_corona_nodes.iterrows():
    if level['Levels'] == "Level 1":
        c_level1.append(level['Nodes'])
    elif level['Levels'] == "Level 2":
        c_level2.append(level['Nodes'])
    elif level['Levels'] == "Level 3":
        c_level3.append(level['Nodes'])
    elif level['Levels'] == "Level 4":
        c_level4.append(level['Nodes'])
    elif level['Levels'] == "Level 5":
        c_level5.append(level['Nodes'])
        
rootlevel_influenza_nodes = pd.read_excel("outputs/rootlevel_influenza_nodes.xlsx")

i_level1 = []
i_level2 = []
i_level3 = []
i_level4 = []
i_level5 = []

for index, level in rootlevel_influenza_nodes.iterrows():
    if level['Levels'] == "Level 1":
        i_level1.append(level['Nodes'])
    elif level['Levels'] == "Level 2":
        i_level2.append(level['Nodes'])
    elif level['Levels'] == "Level 3":
        i_level3.append(level['Nodes'])
    elif level['Levels'] == "Level 4":
        i_level4.append(level['Nodes'])
    elif level['Levels'] == "Level 5":
        i_level5.append(level['Nodes'])

    
    
fig, axes = plt.subplots(1, 2, figsize=(24, 12))  

reduced_colors_subg1 = []
reduced_colors_subg2 = []

for node in reduced_subgraph1.nodes():
    if node in c_level1:
        reduced_colors_subg1.append('red')
    elif node in c_level2:
        reduced_colors_subg1.append('blue')
    elif node in c_level3:
        reduced_colors_subg1.append('green')
    elif node in c_level4:
        reduced_colors_subg1.append('purple')
    elif node in c_level5:
        reduced_colors_subg1.append('orange')
    else:
        reduced_colors_subg1.append('black')
for node in reduced_subgraph2.nodes():
    if node in i_level1:
        reduced_colors_subg2.append('red')
    elif node in i_level2:
        reduced_colors_subg2.append('blue')
    elif node in i_level3:
        reduced_colors_subg2.append('green')
    elif node in i_level4:
        reduced_colors_subg2.append('purple')
    elif node in i_level5:
        reduced_colors_subg2.append('orange')
    else:
        reduced_colors_subg2.append('black')


# Assign colors to levels
level_colors = {
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'purple',
    5: 'orange'
}
        
pos1 = nx.spring_layout(reduced_subgraph1)
pos2 = nx.spring_layout(reduced_subgraph2)
for level, color in level_colors.items():
    plt.scatter([], [], color=color, label=f'Level {level}', s=300, edgecolor='black')

nx.draw(reduced_subgraph1, pos1, ax=axes[0], with_labels=False, node_size=80,  node_color = reduced_colors_subg1,edge_color='black', width=0.1)

plt.legend(scatterpoints=1, frameon=True, title='DFS Levels', bbox_to_anchor=(1.0, 1.0), prop={'size': 20})


nx.draw(reduced_subgraph2, pos2, ax=axes[1], with_labels=False, node_size=80,  node_color = reduced_colors_subg2,edge_color='black',width=0.1)

# Set titles for subplots
axes[0].set_title('Subgraph SARS-CoV-2',fontsize=20)
axes[1].set_title('Subgraph (H1N1) Influenza',fontsize=20)


combined_graph = "figures/After DFS nodes with level in reduced graph.png"
plt.savefig(combined_graph, dpi=300, bbox_inches='tight')



plt.tight_layout()  # Adjust layout for better spacing
plt.show()

# print(reduced_subgraph1)
# print(reduced_subgraph2)