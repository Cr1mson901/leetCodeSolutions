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
                try:
                    temp = str(itr.data)
                except:
                    pass
                llstr += temp + "-->"
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

    def insert_values(self,values=[]):
        self.head = None
        # Can reverse and use insert_at_end or regular and insert_at_beginning
        for value in reversed(values):
            self.insert_at_beginning(value)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self,idx):
        if idx >= self.get_length() or idx < 0:
            raise Exception("Indexing Error")
        elif idx == 0:
            self.head = self.head.next
        else:    
            itr = self.head
            count = 0
            while itr:
                if count == idx - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1
    
    def insert_at(self,idx,data):
        if idx > self.get_length() or idx < 0:
            raise Exception("Indexing Error")
        elif idx == 0:
            self.insert_at_beginning(data)
        else:
            itr = self.head
            count = 0
            while itr:
                if count == idx - 1:
                    itr.next = Node(data,itr.next)
                    break
                itr = itr.next
                count += 1

    def insert_after_value(self, data_after, data_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_insert,itr.next)
                return
            itr = itr.next
        raise Exception('Value was not found in your linked list')
    
    def remove_value(self, data):
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next
        raise Exception('Value was not found in your linked list')

test = LinkedList()
test.insert_at_beginning(8)
test.insert_at_beginning(9)
test.print()
test.insert_at_end(89)
test.print()
test.insert_values([1,2,3,4,65])
test.print()
print(test.get_length())
test.remove_at(0)
test.print()
test.remove_at(2)
test.print()
test.insert_at(1,7)
test.insert_at(4,'Test')
test.print()
test.insert_after_value(65,90)
test.remove_value(65)
test.print()