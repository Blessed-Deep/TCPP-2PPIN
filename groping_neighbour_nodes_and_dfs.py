import ast
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

rootlevel_nodes = []

class Node:
    previousvertices =[]
    vertex = []
    childvertices = []

def NeighborVertexIndex( matrix ):
    return [ index for index, value in enumerate(matrix) if value == 1]

def Grouping(vertices, NeighborVerticesIndex, previousvertices):
    group = []
    for i in range(0, len(NeighborVerticesIndex)):
        group.append([])
    for i in NeighborVerticesIndex:
        if CanVertexAddedToBranch(vertices[i], previousvertices):
            for g in group:
                if len(g) == 0:                    
                    g.append( vertices[i] )                
                    break
                else:                    
                    if CanVertexAddedToGroup(vertices[i], g):
                        g.append( vertices[i] )
                        break
    return group

def CanVertexAddedToBranch(vertex, parentvertices):
    g = []
    h = []
    for i in parentvertices: 
        x = list(ast.literal_eval(i))        
        g.append(x[0])
        h.append(x[1])
    x = list(ast.literal_eval(vertex))
    if (x[0] not in g) and (x[1] not in h):
        return True
    return False

def CanVertexAddedToGroup(vertex, existingvertices):
    for i in existingvertices:
        if not(IsGroupingRuleMatch(vertex, i)):
            return False
    return True

def IsGroupingRuleMatch( vertex1, vertex2 ):
    v1 = list(ast.literal_eval(vertex1))
    v2 = list(ast.literal_eval(vertex2))
    lp, lq = v1[0], v1[1]
    lm, ln = v2[0], v2[1]
    if lp[1:] != lm[1:] and lq[1:] != ln[1:]:
        return True
    return False

def DFS(rootNode, vertices, matrix, DFS_edges):
    print("Root : ", rootNode.vertex)
    rootlevel_nodes.append(rootNode.vertex)
    neighborVertexIndex = []    
    for i in rootNode.vertex:        
        rootIndex = vertices.index(i)
        neighborVertexIndex += NeighborVertexIndex(matrix[rootIndex])
        rootNode.previousvertices.append(i)
    print("child : ", Grouping(vertices, neighborVertexIndex, rootNode.previousvertices ))
    print("")
    
    grp = Grouping(vertices, neighborVertexIndex, rootNode.previousvertices)
    i = grp[0]
    
    if len(i) > 0:
        node = Node()
        node.vertex = i[:]
        node.previousvertices = rootNode.previousvertices
        DFS_edges.append( ("&".join(rootNode.vertex), "&".join(node.vertex)) )
        rootNode.childvertices.append( node )
        DFS(node, vertices, matrix, DFS_edges)

import networkx as nx
import numpy as np

rootNode = Node()
rootNode.vertex.append('(\'P0DTD8\', \'P03470\')')

# Get the adjacency matrix as a NumPy array

vertices = list(tpg.nodes())
matrix = nx.linalg.graphmatrix.adjacency_matrix(tpg).toarray()
DFS_edges = []


DFS(rootNode, vertices, matrix, DFS_edges)

# DFS Figure

tpg_outputGraph = nx.Graph().to_undirected()
tpg_outputGraph.add_edges_from( DFS_edges )
pos = nx.spring_layout(tpg_outputGraph)  
nx.draw(tpg_outputGraph, pos, with_labels=True, node_size=100,font_size=10)

combined_graph = "figures/dfs graph from root_node.png"
plt.savefig(combined_graph, dpi=300, bbox_inches='tight')


corona_df = pd.DataFrame(columns=['Nodes', 'Levels'])
influenza_df = pd.DataFrame(columns=['Nodes', 'Levels'])

level = 0

for i in rootlevel_nodes:
    level += 1
    for j in i:
        x = list(ast.literal_eval(j))
        corona_df = corona_df.append({'Nodes': x[0], 'Levels': f'Level {level}'}, ignore_index=True)
        influenza_df = influenza_df.append({'Nodes': x[1], 'Levels': f'Level {level}'}, ignore_index=True)

tpg_edges = [{'Source': source, 'Target': target} for source, target in tpg_outputGraph.edges()]
edges_df = pd.DataFrame(tpg_edges)


edges_df.to_csv('outputs/DFS_edges.csv', index=False)
corona_df.to_excel("outputs/rootlevel_corona_nodes.xlsx", index=False)
influenza_df.to_excel("outputs/rootlevel_influenza_nodes.xlsx", index=False)