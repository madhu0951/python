class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insert_front(self,data):
        new_node=Node(data)
        new_node.next = self.head
        if self.head is None:
            self.head=new_node
        self.head=new_node
    def insert_middle(self,prev_node,data):
        new_node=Node(data)
        new_node.next=prev_node.next
        new_node.prev=prev_node
        prev_node.next=new_node
        if new_node.next:
            new_node.next.prev=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=new_node
        new_node.prev=itr
        return

    def display(self,node):
        while node:
            print(node.data,end="->")
            last=node
            node=node.next
dlist=DoublyLinkedList()
dlist.insert_front(5)
dlist.insert_front(6)
dlist.insert_front(7)
dlist.insert_middle(dlist.head.next,10)
dlist.insert_end(15)
dlist.insert_end(18)
dlist.display(dlist.head)
