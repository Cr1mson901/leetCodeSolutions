class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if not self.head:
            print("This linked list is empty")
        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr += str(itr.data) + "-->"
                itr = itr.next
            print(llstr)
    
    def insert_at_end(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data)

test = LinkedList()
test.insert_at_beginning(8)
test.insert_at_beginning(9)
test.print()
test.insert_at_end(89)
test.print()