"""
    Title:          Implementation of MinHeap
    Author:         Keivan Ipchi Hagh
    Version:        Python 3.8.1
    Date Created:   Sunday, January 31, 2021
    GitHub:         https://github.com/keivanipchihagh

    Description:    Modified MinHeap module for the final project for 'Data Structures & Algorithms'. 
"""

# Imports
import sys
from HashTable import HashTable


class MinHeap:
    """ MinHeap class """


    def __init__(self, max_size):
        """ Constructor """

        # Size variables
        self.max_size = max_size
        self.size = 0

        # Heap
        self.heap = [[]] * (self.max_size + 1)
        self.heap[0] = [-1 * sys.maxsize]

        # HashTable
        self.hash_table = HashTable()


    def get_parent(self, index):
        """ Returns the parent index """

        return index // 2


    def get_left_child(self, index):
        """ Returns the left child index """

        return 2 * index


    def get_right_child(self, index):
        """ Returns the right child index """

        return 1 + (2 * index)


    def is_leaf(self, index):
        """ Determines whether index is a leaf or not """

        return self.size // 2 <= index < self.size


    def swap(self, index_1, index_2):
        """ Swaps two indexes """

        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]                 # Swap heap
            
        self.hash_table.add_range([[self.heap[index_1][1], index_1], [self.heap[index_2][1], index_2]])   # Update HashTable


    def print(self):
        """ Prints the heap """

        print(self.heap)


    def get_heap(self):
        """ Returns the heap """

        return self.heap


    def heapify(self, index):
        """ Heapifies the heap """

        # Get left & right children
        left_child, right_child = self.get_left_child(index), self.get_right_child(index)

        if (left_child < self.size and right_child < self.size and not self.is_leaf(index)):
            
            swapper = left_child if (self.heap[left_child][0] < self.heap[right_child][0]) else right_child
            
            self.swap(swapper, index)       # Swap

            self.heapify(swapper)           # Recursive here!


    def add(self, value, node):
        """ Adds a value to the heap """

        if self.size >= self.max_size:
            print("Max Size Reached!")
            return

        self.size += 1                              # Increment size
        self.heap[self.size] = [value, node]        # Set value

        self.hash_table.add(node, self.size)    # Add to HashTable

        current = self.size

        while self.heap[current][0] < self.heap[self.get_parent(current)][0]:
            self.swap(current, self.get_parent(current))
            current = self.get_parent(current)


    def add_range(self, items):
        """ Adds a list of node/values into the heap """

        for node in items.keys():
            self.add(items[node], node)


    def pop(self):
        """ Pops the minimum value in the heap """

        popped = self.heap[1][0]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heapify(1)

        return popped


    def get_min(self):
        """ Returns the minimum value in the heap """

        return self.heap[1]


    def clear(self):
        """ Clears the heap """        

        # Reset HashTable
        self.hash_table.clear()

        # Reset heap
        self.size = 0
        self.heap = [0] * (self.max_size + 1)
        self.heap[0] = [-1 * sys.maxsize]


    def update(self, node, new_value):
        """ Updates a value in the heap """

        index = self.hash_table.get(node)   # Get index

        self.remove(index)             # Remove the spesific index
        self.add(new_value, node)      # Add the new value


    def print_hash_table(self):
        """ Prints the hash table """

        print(self.hash_table.table)


    def get_node_min(self):
        """ Returns the node id for the minimum value in the heap """

        min = self.get_min()
        return min[1]


    def remove(self, index):
        """ Removes a spesific index """

        index_to_delete = self.heap[index]        
        self.heap[index] = self.heap[self.size]
        self.size -= 1
        self.heapify(index)     # Heapify

        return index_to_delete[1]
