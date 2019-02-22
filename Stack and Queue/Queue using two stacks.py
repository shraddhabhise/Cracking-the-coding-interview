class queue:
    def __init__(self):
        self.stack1=[]
        self.stack2 = []

    def enque(self, x):
        self.stack1.append(x)
    def deque(self):
        if self.stack2:
            while len(self.stack2)>0:
                self.stack1.append(self.stack2.pop())
            while len(self.stack1)>1:
                self.stack2.append(self.stack1.pop())
            return self.stack1.pop()
        if not self.stack2 and self.stack1:
            while len(self.stack1)>1:
                self.stack2.append(self.stack1.pop())
            return self.stack1.pop()

    def top(self):
        if self.stack2:
            while len(self.stack2)>0:
                self.stack1.append(self.stack2.pop())
            while len(self.stack1) > 1:
                self.stack2.append(self.stack1.pop())
            return self.stack1[0]
        if not self.stack2 and self.stack1:
            while len(self.stack1) > 1:
                self.stack2.append(self.stack1.pop())
            return self.stack1[0]

    def empty(self):
        return not self.stack1 and not self.stack2

obj= queue()
print ("Iempty :", obj.empty())
obj.enque(1)
obj.enque(2)
obj.enque(3)
obj.enque(4)
obj.enque(5)

print ("popped element is:", obj.deque())
print ("popped element is:", obj.deque())

print ("Top is:", obj.top())
obj.enque(6)
obj.enque(7)
print ("popped element is:", obj.deque())

print ("Iempty :", obj.empty())