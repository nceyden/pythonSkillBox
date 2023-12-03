class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class Stack:
    def __init__(self):
        self.end = None  

    def pop(self):
        if self.end is None:
            raise IndexError("empty stack")
        val = self.end.data
        self.end = self.end.next
        return val

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.end
        self.end = new_node

    def print(self):
        current = self.end
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
