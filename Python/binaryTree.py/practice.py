import collections
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

#Left, Root, Right
def inOrderPrint(r):
    if r is None:
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end=" ")
        inOrderPrint(r.right)

#Root, Left, Right
def preOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end=" ")
        preOrderPrint(r.left)
        preOrderPrint(r.right)
    
#Root, Right, Left    
def postOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end=" ")
        postOrderPrint(r.right)
        postOrderPrint(r.left)

#Bredth First Search using Adjacency List
def bfs(al):
    visited = []
    queue = collections.deque('g')
    while queue:
        node = queue.popleft()
        visited.append(node)
        [queue.append(x) for x in al[node]]
    print(visited)

# #Bredth First Search / What I came up with
# def bfs(r,queue=[],visited=[]):
    # visited.append(queue.pop(0).data)
    # if r.left is not None:
    #     queue.append(r.left)
    # if r.right is not None:
    #     queue.append(r.right)
    # for item in queue:
    #     bfs(item, queue, visited)
    # return visited

#Adjacency List 
def makeList(r):
    if r is None:
        return
    else:
        d[r.data] = []
        if r.left:
            d[r.data].append(r.left.data)
            makeList(r.left)
        if r.right:
            d[r.data].append(r.right.data)
            makeList(r.right)
    return d



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
print("\n")
preOrderPrint(root)
print('\n')
postOrderPrint(root)
print('\n')

d = {}

alist = makeList(root)
for item in alist.items():
    print(item)

bfs(alist)