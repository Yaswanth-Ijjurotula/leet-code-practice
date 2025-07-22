# Approach using two queues for implementing stack.
# from queue import Queue
# class Stack:
#     def __init__(self):
#         self.q1 = Queue()
#         self.q2 = Queue()
#         self._size = 0
#     def push(self,x):
#         self.q2.put(x)
#         self._size+=1
#         while not self.q1.empty():
#             self.q2.put(self.q1.get())
#         self.q1,self.q2 = self.q2,self.q1

#     def pop(self):
#         if self.empty():
#             return -1
#         self._size -= 1
#         return self.q1.get()

#     def top(self):
#         if self.empty():
#             return -1
#         ele = self.q1.get()
#         self.push(ele)
#         self._size -=1
#         return ele
#     def size(self):
#         return self._size
    
#     def empty(self):
#        return self._size == 0

# Approach-2 (using deque DS)
# from collections import deque
# class Stack:
#     def __init__(self):
#         self.q1 = deque()
#         self.q2 = deque()
#     def push(self,x):
#         # pushing element on to the q2
#         self.q2.append(x)
#         while self.q1:
#             self.q2.append(self.q1.popleft())
#         self.q1,self.q2 = self.q2,self.q1

#     def pop(self):
#         if self.empty():
#             return -1
#         return self.q1.popleft()

#     def top(self):
#         if self.empty():
#             return -1
#         return self.q1[0]
#     def size(self):
#         return len(self.q1)
    
#     def empty(self):
#        return not self.q1

# Approach using a single queue to implement stack
from collections import deque
class Stack:
    def __init__(self):
        self.q1 = deque()

    def push(self,x):
        self.q1.append(x)
        l = len(self.q1) - 1
        while (l):
            self.q1.append(self.top())
            self.q1.popleft()
            l -= 1
    def pop(self):
        if not len(self.q1):
            return -1
        return self.q1.popleft()
    def top(self):
        if self.empty():
            return -1
        return self.q1[0]
    def empty(self):
         return not self.q1
    def size(self):
        return len(self.q1)
if __name__ == "__main__":
    my_stack = Stack()

    print("--- Initial State ---")
    print(f"Is stack empty? {my_stack.empty()}") # Expected: True
    print(f"Stack size: {my_stack.size()}")     # Expected: 0
    print(f"Popping from empty stack: {my_stack.pop()}") # Expected: -1
    print(f"Top of empty stack: {my_stack.top()}")       # Expected: -1

    print("\n--- Pushing elements ---")
    my_stack.push(10)
    print(f"Pushed 10. Top: {my_stack.top()}, Size: {my_stack.size()}") # Top: 10, Size: 1
    my_stack.push(20)
    print(f"Pushed 20. Top: {my_stack.top()}, Size: {my_stack.size()}") # Top: 20, Size: 2
    my_stack.push(30)
    print(f"Pushed 30. Top: {my_stack.top()}, Size: {my_stack.size()}") # Top: 30, Size: 3

    print("\n--- Peeking at top ---")
    current_top = my_stack.top()
    print(f"Current top element: {current_top}") # Expected: 30
    print(f"Stack size after top: {my_stack.size()}") # Expected: 3 (should not change)

    print("\n--- Popping elements ---")
    popped_val = my_stack.pop()
    print(f"Popped: {popped_val}. Top: {my_stack.top()}, Size: {my_stack.size()}") # Popped: 30, Top: 20, Size: 2

    popped_val = my_stack.pop()
    print(f"Popped: {popped_val}. Top: {my_stack.top()}, Size: {my_stack.size()}") # Popped: 20, Top: 10, Size: 1

    print("\n--- Final operations ---")
    print(f"Is stack empty? {my_stack.empty()}") # Expected: False
    popped_val = my_stack.pop()
    print(f"Popped: {popped_val}. Top: {my_stack.top()}, Size: {my_stack.size()}") # Popped: 10, Top: -1, Size: 0
    print(f"Is stack empty? {my_stack.empty()}") # Expected: True

    print(f"Popping from empty stack again: {my_stack.pop()}") # Expected: -1