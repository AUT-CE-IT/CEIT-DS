"""
    Title:          Main
    Author:         Keivan Ipchi Hagh
    Version:        Python 3.8.1
    Date Created:   Sunday, January 31, 2021
    GitHub:         https://github.com/keivanipchihagh

    Description:    Driver file for the final project for 'Data Structures & Algorithms'
"""

# Imports
import math
from Dijkstra import dijkstra
from DataReader import read

def get_distance(src, dest):
    """ Calculates & returns the distance between the two nodes """

    return math.sqrt(((src[0] - dest[0]) ** 2) + ((src[1] - dest[1]) ** 2))


# Driver Code
if __name__ == "__main__":

    path = 'm1.txt'

    graph, points, edges, nodes_count = read(path)          # Reads the input file and returns the constructed Graph

    user_input = [x for x in input().split(' ')]

    dijkstra(graph, user_input[1], user_input[2], nodes_count)