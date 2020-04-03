class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def add(self,data):
        while len(self.stack2)>0:
            self.stack1.append(self.stack2.pop(0))
        self.stack1.append(data)
    def get(self):
        while len(self.stack1)>0:
            self.stack2.append(self.stack1.pop())
        if len(self.stack2) > 0:
            return self.stack2.pop(0)
        else:
            return -1


q=Queue()
q.add(1)
q.add(2)
q.add(3)

q.add(5)
q.add(6)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
q.add(4)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
