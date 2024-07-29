# 1. Define a Tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    #Function for inserting data. Less then goes to the left. Greater then on the right
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node
                else:
                    self.right.insert(data)