# Approach-1

# from queue import LifoQueue

# class Queue:
#     def __init__(self):
#         self.input = LifoQueue()
#         self.output = LifoQueue()


#     def push(self, data: int) -> None:
#         # Pop out all elements from the stack input
#         while not self.input.empty():
#             self.output.put(self.input.get())
#         # Insert the desired element in the stack input
#         print("The element pushed is", data)
#         self.input.put(data)
#         # Pop out elements from the stack output and push them into the stack input
#         while not self.output.empty():
#             self.input.put(self.output.get())


#     # Pop the element from the Queue
#     def pop(self) -> int:
#         if self.input.qsize() == 0:
#             print("Stack is empty")
#             exit(0)
#         val = self.input.get()
#         return val


#     def Top(self) -> int:
#         if self.input.qsize() == 0:
#             print("Stack is empty")
#             exit(0)
#         return self.input.queue[-1]


#     def size(self) -> int:
#         return self.input.qsize()

# Approach - 2
from queue import LifoQueue

class MyQueue:
    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()


    # Push element x to the back of queue.
    def push(self, x: int) -> None:
        print("The element pushed is ", x)
        self.input.put(x)


    # Removes the element from in front of queue and returns that element.
    def pop(self) -> int:
        # shift input to output
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())
        x = self.output.get()
        return x


    # Get the front element.
    def top(self) -> int:
        # shift input to output
        if self.output.empty():
            while not self.input.empty():
                self.output.put(self.input.get())
        return self.output.queue[-1]


    def size(self) -> int:
        return self.input.qsize() + self.output.qsize()



if __name__ == "__main__":
     q = MyQueue()
     q.push(3)
     q.push(4)
     print("The element poped is", q.pop())
     q.push(5)
     print("The top of the queue is", q.top())
     print("The size of the queue is", q.size())

