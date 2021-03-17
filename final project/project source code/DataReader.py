"""
    Title:          Implementation of DataReader
    Author:         Keivan Ipchi Hagh
    Version:        Python 3.8.1
    Date Created:   Sunday, January 31, 2021
    GitHub:         https://github.com/keivanipchihagh

    Description:    DataReader for the final project for 'Data Structures & Algorithms'
"""

# Imports
import math


def get_distance(src, dest):
    """ Calculates & returns the distance between the two nodes """

    return math.sqrt(((src[0] - dest[0]) ** 2) + ((src[1] - dest[1]) ** 2))


def read(path):
    """ Reads the file and returs the graph """

    # Variables
    nodes = {}
    graph = {}

    # Variables for MatPlotLib
    points = {}
    edges = []

    with open(path, 'r') as file:

        # Get node & edge count
        node_count, edge_count = [int(entry)
                                  for entry in file.readline().split(' ')]

        # Get nodes & their corresponding coordinates
        for i in range(node_count):
            entry = [x for x in file.readline().split(' ')]
            nodes[entry[0]] = [float(x) for x in entry[1:]]

            points[entry[0]] = [entry[1], entry[2]]


        # Get edges, calculate their distances and add to the graph
        for i in range(edge_count):
            src, dest = [x.strip() for x in file.readline().split(' ')]
            edges.append([src, dest])

            # Calculate the distance between the two nodes
            distance = get_distance(nodes[src], nodes[dest])

            # Make a new dictionary if node does not already exist in the graph
            if src not in graph.keys():
                graph[src] = {}

            graph[src][dest] = distance

    fixed_graph = fix_graph(graph, nodes)  # Fix the graph format

    return fixed_graph, points, edges, node_count


def fix_graph(graph, nodes):
    """ Fixes the graph - Adds starting nodes if not already existing """

    for node in nodes:
        if not node in graph.keys():
            graph[node] = {}

    return graph