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
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    # def print(self):
    #     # An Interesting way to display the heirarchy of the tree
    #     # receipt = []
    #     # if self.left:
    #     #     receipt.append(self.left.print())
    #     # receipt.append(self.data)
    #     # if self.right:
    #     #     receipt.append(self.right.print())
    #     # return receipt

def inOrderPrint(r):
    if r is None:
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end=" ")
        inOrderPrint(r.right)



    

root = Node('g')
root.insert('c')
root.insert('b')
root.insert('a')
root.insert('e')
root.insert('d')
root.insert('f')
root.insert('i')
root.insert('h')
root.insert('j')
root.insert('k')
inOrderPrint(root)