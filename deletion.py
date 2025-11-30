class NODE:
    def __init__(self,data):
        self.data = data
        self.next = None
    
a= NODE(2)
b= NODE(21)
c= NODE(32)
d= NODE(7)

head = a

a.next =b
b.next = c
c.next =d

def printLinkedlist(head):
    curr = head
    while curr!=None:
        print(curr.data,end =" ")
        curr = curr.next


def deletion_beg(head):
      return head.next

head= deletion_beg(head)
printLinkedlist(head)

def deletion_end(head):
    curr = head
    while curr.next.next!= None:
        curr= curr.next
    curr.next = None

deletion_end(head)
printLinkedlist(head)

def deletionAt_k(head,k):
    curr = head
    for i in range(k-2):
        curr = curr.next
    curr.next = curr.next.next

deletionAt_k(head,3)
printLinkedlist(head)