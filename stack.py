"""Create Stack object"""

class StackUnderflowError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class StackOverflowError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidCapacityError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Stack:
    def __init__(self, capacity):
        if capacity >= 0:
            self.capacity = capacity
            self.values = []
        else:
            raise InvalidCapacityError("Capacity must be greater than or \
            equal to zero.")

    def is_empty(self):
        return len(self.values) == 0

    def push(self, value):
        if len(self.values) < self.capacity:
            self.values.append(value)
        else:
            raise StackOverflowError("Your stack is at capacity")

    def pop(self):
        if self.values:
            self.values.pop(-1)
        else:
            raise StackUnderflowError("Stack is empty!")

    def len(self):
        return len(self.values)

    def peek(self):
        if self.values:
            return self.values
        else:
            return None

    def find(self, value):
        while self.values[-1] != value:
            self.pop()
        return self.values[-1]    
