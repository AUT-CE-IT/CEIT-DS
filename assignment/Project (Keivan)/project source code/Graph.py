"""
    Title:          Implementation of Graph
    Author:         Keivan Ipchi Hagh
    Version:        Python 3.8.1
    Date Created:   Sunday, February 1, 2021
    GitHub:         https://github.com/keivanipchihagh

    Description:    Graph for the final project for 'Data Structures & Algorithms'
"""

# Imports
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab


def get_weight(src, dest, path):

    src_index, dest_index = 0, 0

    try: src_index = path.index(src)
    except: pass
    try: dest_index = path.index(dest)
    except: pass

    return (len(path) - (src_index + 1)) if (src_index + 1 == dest_index) else 0

def draw(graph, path):
    """ Draws a graph """

    G = nx.DiGraph()

    # Add edges
    for key in graph.keys():
        for item in graph[key].items():
            G.add_edges_from([(key, item[0])], weight = get_weight(key, item[0], path))

    # Highlight path
    val_map = {}

    for node in path:
        val_map[node] = 0.5

    values = [val_map.get(node, 0.7) for node in G.nodes()]

    edge_labels = dict([((u, v), d['weight']) for u, v, d in G.edges(data = True)])

    node_labels = {node:node for node in G.nodes()}

    red_edges = []
    for i in range(len(path) - 1):
        red_edges.append((path[i], path[i + 1]))

    edge_colors = ['green' if not edge in red_edges else 'red' for edge in G.edges()]

    pos = nx.spring_layout(G)

    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)
    nx.draw_networkx_labels(G, pos, labels = node_labels)

    nx.draw(G, pos, node_color = values, node_size = 500, edge_color = edge_colors, edge_cmap = plt.cm.Reds)

    pylab.show()