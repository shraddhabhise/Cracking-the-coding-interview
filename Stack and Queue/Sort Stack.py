class Solution:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.tempstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return None
        else:
            return self.stack.pop()

    def top(self, st):
        """
        :rtype: int
        """
        if st:
            return st[-1]
        else:
            return None

    def sort(self):
        """
        :rtype: int
        """
        while len(self.stack)>0:
            tmp = self.stack.pop()
            while len(self.tempstack)>0 and tmp < self.top(self.tempstack):
                self.stack.append(self.tempstack.pop())
            self.tempstack.append(tmp)

        return self.tempstack

obj= Solution()
obj.push(34)
obj.push(3)
obj.push(31)
obj.push(98)
obj.push(92)
obj.push(23)

print ("stack is:", obj.stack)

print ("sorted stack is:", obj.sort())



