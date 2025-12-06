class stack:
    def __init__(self):
        self.s= []
    
    def push(self,x):
        return self.s.append(x)
    
    def pop(self):
        if len(self.s)== 0:
            print("Stack underflow")
            return None
        return self.s.pop()
    
    def peek(self):
        if len(self.s)== 0:
            print("stack is empty")
            return None
        return self.s[-1]
        
    
    def isEmpty(self):
        return len(self.s)== 0
    
    def display(self):
        return print("stack:- ",self.s)
    
k=stack()
k.push(3)
k.push(10)
k.push(1)
k.push(5)

k.display()

print("popped ",k.pop())
k.display()

print("peek",k.peek())