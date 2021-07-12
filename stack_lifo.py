#  LIFO stack implementation using a Python list as 
# its underlying storage.

class StackADT:
    # Create an empty stack.
    def __init__(self):
        self.data = []

    # Add element e to the top of the stack 
    def push(self, e):
        self.data.append(e)

    # Remove and return the element from the top of the stack 
    # (i.e., LIFO). Raise exception if the stack is empty.
    def pop(self):
        if self.data.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data.pop()


    # Return (but do not eremove) the element at the top of
    # the stack. Raise Empty exception if the stack is empty. 
    def peek(self):
        if self.data.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data[-1]

    # Return True if the stack is empty
    def is_empty(self):
        return len(self.data) == 0

    # Return the number of elements in the stack
    def size(self):
        return len(self.data)