"""
    Title:          Implementation of HashTable
    Author:         Keivan Ipchi Hagh
    Version:        Python 3.8.1
    Date Created:   Sunday, February 2, 2021
    GitHub:         https://github.com/keivanipchihagh

    Description:    HashTable module for the final project for 'Data Structures & Algorithms'. 
"""

class HashTable:
    """ HashTable class """

    def __init__(self):
        """ Constructor """

        self.table = {}


    def add(self, key, value):
        """ Adds a key/value pair to the table """

        self.table[key] = value


    def add_range(self, items):
        """ Adds a list of items into the table as value/index """

        for node, value in items:
            self.add(node, value)


    def remove(self, key):
        """ Removes a key/value pair from the table """

        del self.table[key]

    
    def pop(self, key):
        """ Returns the value for the given key, also removes the key from the table """

        return self.table.pop(key)


    def get_value(self, key):
        """ Returns the vale for the given key """

        try:
            return self.table[key]
        except:
            raise Exception("Key not found")


    def print(self):
        """ Prints the table """

        print(self.table)


    def clear(self):
        """ Clears the table """

        self.table = {}    


    def get(self, key):
        """ Returns a value """

        return self.table.get(key)