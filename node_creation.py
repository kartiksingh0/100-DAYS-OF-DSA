class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a= Node(5)
b = Node(7)
c = Node(17)
d = Node(337)


head = a
a.next =b
b.next =c
c.next = d

def printLinkedlist(head):
        curr = head
        while curr!= None:
             print(curr.data , end = " ")
             curr= curr.next

printLinkedlist(head)
