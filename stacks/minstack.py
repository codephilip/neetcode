class MinStack(object):

    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        self.data.append(val)

    def pop(self):
        """
        :rtype: None
        """
        x = self.data.pop()
        if x == self.min[-1]:
            self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
