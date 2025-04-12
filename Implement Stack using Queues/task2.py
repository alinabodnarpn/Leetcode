from collections import deque
class MyStack(object):
    """
    A stack implementation using two deques
    """

    def __init__(self):
        self.main_queue = deque()
        self.temp_queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.temp_queue.append(x)
        while self.main_queue:
            self.temp_queue.append(self.main_queue.popleft())
        self.main_queue, self.temp_queue = self.temp_queue, self.main_queue

    def pop(self):
        """
        :rtype: int
        """
        return self.main_queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.main_queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.main_queue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
