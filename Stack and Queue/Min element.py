class Solution:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.min) == 0 or x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return None
        else:
            x = self.stack.pop()
            # if len(self.min):
            if self.min and x == self.min[-1]:
                self.min.pop()
            return x

    def peek(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]
        else:
            return None

obj= Solution()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print ("stack is:", obj.stack)

print ("popped element is:", obj.pop())

print ("peek is:", obj.peek())

print ("min is:", obj.getMin())


