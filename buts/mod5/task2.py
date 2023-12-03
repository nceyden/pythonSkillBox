class Node:
    def __init__(self, data):
        self.data = data  
        self.nref = None  
        self.pref = None  

class Stack:
    def __init__(self):
        self.top = None  

    def pop(self):
        if self.top is None:
            return None
        else:
            val = self.top.data
            self.top = self.top.pref
            return val

    def push(self, val):
        new_node = Node(val)
        new_node.pref = self.top
        self.top = new_node

    def print(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.pref
        print()
