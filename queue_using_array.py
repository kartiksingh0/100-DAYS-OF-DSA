class queue:
    def __init__(self):
        self.q =[]
        self.front = -1

    def push(self,x):
        if self.front == -1:
            self.front = 0

        self.q.append(x)

    def pop(self):
        if len(self.q)==0:
            return -1
        
        x= self.q[self.front]
        self.front += 1
        if self.front == len(self.q):
            self.front = -1
            self.q =[]
        return x
    
      
    def getFront(self):
        if not self.q:
            return -1
        return self.q[0]
    
    def getSize(self):
        return len(self.q)
    
    def display(self):
         a= []
         if self.front == -1:
          print("Queue is empty")
          return
    
         for i in range(self.front, len(self.q)):
             a.append(self.q[i])
         return a

q= queue()
q.push(5)
q.push(6)
q.push(8)


print(q.display())
