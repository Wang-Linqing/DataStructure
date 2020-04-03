class Stack():
    def __init__(self):
        self.stack=[]
        self.min_stack=[]
    def pop(self):
        if len(self.stack)==0:
            return None
        self.min_stack.pop()
        return self.stack.pop()
    def push(self,data):
        if len(self.stack)==0:
            self.min_stack.append(data)
            self.stack.append(data)
        else:
            self.stack.append(data)
            if data<self.min_stack[-1]:
                self.min_stack.append(data)
            else:
                self.min_stack.append(self.min_stack[-1])
    def min(self):
        if len(self.min_stack)==0:
            return None
        return self.min_stack[-1]
if __name__=="__main__":
    s=Stack()
    s.push(3)
    print(s.stack)
    print("min",s.min_stack)
    s.push(4)
    print(s.stack)
    print("min",s.min_stack)
    s.push(-1)
    print(s.stack)
    print("min",s.min_stack)
    s.push(2)
    print(s.stack)
    print("min",s.min_stack)
    s.push(2)
    print(s.stack)
    print("min",s.min_stack)
    s.push(-2)
    print(s.stack)
    print("min",s.min_stack)
    print(s.pop())
    print(s.stack)
    print("min",s.min_stack)
    print(s.pop())
    print(s.stack)
    print("min",s.min_stack)
    print(s.pop())
    print(s.stack)
    print("min",s.min_stack)
