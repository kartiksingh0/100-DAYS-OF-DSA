class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self,x):
        self.length += 1
        if self.top is None:
            self.top = node(x)
            return
        
        else:
            newNode = node(x)
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        if self.top == None:
            return -1
        self.length -=1
        x = self.top.data
        self.top = self.top.next
        return x
    
    def gettop(self):
        if self.top == None:
            return -1
        return self.top.data
    
    def display(self):
        if self.top is None:
            print("stack is empty")
            return
        curr = self.top
        while curr:
            print(curr.data,end=" ")
            curr = curr.next

s = stack()
s.push(3)
s.push(10)
s.push(1)
s.display()
s.pop()
s.display()