class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        min_val = self.getMin()
        if min_val==None or min_val>x:
            min_val = x
        self.mins.append(min_val)
        self.stack.append(x)
        
    def pop(self):
        """
        :rtype: void
        """
        self.mins.pop()
        return self.stack.pop()
        
    def top(self):
        """
        :rtype: void
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: void
        """
        if len(self.mins) == 0:
            return None
        return self.mins[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
assert minStack.getMin()==-3
assert minStack.pop()==-3
assert minStack.top()==0
assert minStack.getMin()==-2