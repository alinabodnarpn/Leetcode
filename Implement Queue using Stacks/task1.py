from collections import deque
class MyQueue:
    """
    A class that implements a queue using two stacks
    """
    def __init__(self):
        """
        Initializes two stacks to implement the queue
        """
        self.input_stack = deque()
        self.output_stack = deque()

    def push(self, x):
        """
        Pushes element x to the back of the queue
        """
        self.input_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of the queue and returns it
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()

    def peek(self):
        """
        Gets the front element of the queue without removing it
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty
        """
        return not self.input_stack and not self.output_stack
