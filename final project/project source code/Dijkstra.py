"""
    Title:          Implementation of Dijkstra
    Author:         Keivan Ipchi Hagh
    Version:        Python 3.8.1
    Date Created:   Sunday, February 1, 2021
    GitHub:         https://github.com/keivanipchihagh

    Description:    Dijkstra's algorithm for the final project for 'Data Structures & Algorithms'
"""

# Imports
import math
from MinHeap import MinHeap
from Weights import Weights
from Graph import draw

def back_track(src, dest, predecessor):
    """ Backtracking algorithm to find the travelled path from source to destination """

    node = dest             # Make a copy of the destination node
    shortest_path = []      # Store shortest path from source to destination    

    while node != src:

        try:
            shortest_path.append(node)      # Add the node to the list
            node = predecessor[node]
        except:
            print("Route not found!")       # Bad luck, I guess?
            break
            
    shortest_path.append(src)           # Add the source to the list
    shortest_path.reverse()      # Return reversed list to make it look more gorgeous

    return shortest_path

def get_travel_time(graph, path):
    """ Calculates & returns the ETA """

    ETA = 0

    for i in range(len(path) - 1):
        ETA += graph[path[i]][path[i + 1]]

    return ETA * 120


def dijkstra(graph, src, dest, nodes_count):
    """ Implementation of Dikstra algorithm """

    unexplored = graph.copy()               # Add the entire graph as unexplored
    shortest_distances = {}                 # Store shortest distances from two nodes    
    predecessor = {}                        # Store visited nodes for back-tracking
    min_heap = MinHeap(nodes_count)         # Min Heap    

    weights_handler = Weights(graph)
    graph = weights_handler.get_weights()   # Update weights

    # Initialize shortest path of every node as INFINITY
    for node in unexplored:
        shortest_distances[node] = math.inf

        if node != src:
            min_heap.add(shortest_distances[node], node)            # Save node's shortest distance in the min heap

    shortest_distances[src] = 0                     # Source has '0' length
    min_heap.add(shortest_distances[src], src)      # Save source's shortest distance in the min heap

    # Running the loop while all the nodes have been visited
    while unexplored:
        
        node_to_visit = None                        # The node we should visit next

        node_to_visit = min_heap.get_node_min()     # Get shortest current distance   

        # Explore all neighbors
        for child_node, value in unexplored[node_to_visit].items():

            # Check if the new path is the shortest discovered yet
            if value + shortest_distances[node_to_visit] < shortest_distances[child_node]:

                shortest_distances[child_node] = value + shortest_distances[node_to_visit]  # Replace the new shortest path

                min_heap.update(child_node, shortest_distances[child_node])

                predecessor[child_node] = node_to_visit                                     # Store the node for backtracking

        unexplored.pop(node_to_visit)       # Node is visited & removed from the 'unexplored' list
        min_heap.pop()                      # Remove the minimum value from heap
        
    # Get the shortest path using backtracking
    shortest_path = back_track(src, dest, predecessor)

    # Check if the target has actually been visited
    if shortest_distances[dest] != math.inf:

        # print("Shortest Distance:\t", str(shortest_distances[dest]))                # Print shortest distance from source to the destination
        print("Shortest Path:\t\t", " -> ".join(shortest_path))                       # Print the shortest path
        # print("Shortest Distances:\t", str(shortest_distances))                     # Print the detailed path
        print("ETA:\t\t\t", "{:.3f}".format(get_travel_time(graph, shortest_path)), "Minutes")         # Prints the ETA

        weights_handler.update_traffic(shortest_path)   # Update the traffic

        draw(graph, shortest_path)                      # Draw plot