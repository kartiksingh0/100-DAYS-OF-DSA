class NODE:
    def __init__(self,data):
        self.data = data
        self.next = None

a = NODE(4)
b = NODE(41)
c = NODE(24)
d = NODE(2)
a.next =b
b.next =c
c.next =d
head =a

def printLinkedlist(head):
    curr = head
    while curr!=None:
        print(curr.data,end = " ")
        curr = curr.next


def insertion_beg(newNode):
    global head
    newNode.next = head
    head = newNode

newNode = NODE(12)
insertion_beg(newNode)
printLinkedlist(head)

def insertion_end(newNode):
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = newNode

newNode = NODE(17)
insertion_end(newNode)
printLinkedlist(head)

def insertionAT_K(newNode,k):
    curr = head
    for i in range(k-1):
        curr= curr.next
    newNode.next = curr.next
    curr.next = newNode

newNode = NODE(72)
insertionAT_K(newNode,4)
printLinkedlist(head)
