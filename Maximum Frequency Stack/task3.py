from collections import deque
class FreqStack:
    """
    A stack implementation using two deques
    """
    def __init__(self):
        self.main_stack = deque()
        self.freq_stacks = deque()
        self.max_freq = 0

    def push(self, value):
        """
        Pushes a value into stack, updating its frequency
        """
        freq = 0
        temp = deque()
        while self.main_stack:
            item = self.main_stack.pop()
            if item[0] == value:
                freq += 1
            temp.append(item)
        while temp:
            self.main_stack.append(temp.pop())
        self.main_stack.append((value, freq + 1))
        while len(self.freq_stacks) <= freq:
            self.freq_stacks.append(deque())
        self.freq_stacks[freq].append(value)
        self.max_freq = max(self.max_freq, freq + 1)

    def pop(self):
        """
        Removes and return most frequent element 
        """
        value = self.freq_stacks[self.max_freq - 1].pop()
        temp_stack = deque()
        found = False
        while self.main_stack:
            item = self.main_stack.pop()
            if not found and item[0] == value and item[1] == self.max_freq:
                found = True
            else:
                temp_stack.append(item)
        while temp_stack:
            self.main_stack.append(temp_stack.pop())
        if not self.freq_stacks[self.max_freq - 1]:
            self.max_freq -= 1
        return value
