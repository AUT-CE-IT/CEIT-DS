"""
    Title:          Implementation of Weights Handler
    Author:         Keivan Ipchi Hagh
    Version:        Python 3.8.1
    Date Created:   Sunday, February 4, 2021
    GitHub:         https://github.com/keivanipchihagh

    Description:    Weights Handler for the final project for 'Data Structures & Algorithms'
"""

class Weights:
    """ Weights class """

    def __init__(self, graph):
        """ Constructor """

        self.graph = graph.copy()     # Make a COPY!
        self.traffic = {}

        for key in self.graph.keys():

            if key not in self.traffic.keys():
                self.traffic[key] = {}

            for item in self.graph[key].items():
                self.traffic[key][item[0]] = 0

    def update_traffic(self, path):
        """ Updates the raffic on the given path """

        for i in range(len(path) - 1):
            src, dest = path[i], path[i + 1]

            self.traffic[src][dest] += 1


    def get_traffic(self):
        """ Returns the current traffic """

        return self.traffic


    def get_weights(self):
        """ Returns the weights for the graph using traffic & length """

        weights = {}

        for key in self.graph.keys():

            if key not in weights.keys():
                weights[key] = {}

            for item in self.graph[key].items():
                weights[key][item[0]] = self.graph[key][item[0]] * (1 + (0.3 * self.traffic[key][item[0]]))    # Update using the formula

        return weights