class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]



if __name__ == "__main__":
    print("--- Test Case 1 ---")
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(f"Current top: {minStack.top()}")   # Expected: -3
    print(f"Current min: {minStack.getMin()}") # Expected: -3
    minStack.pop()
    print(f"After pop, top: {minStack.top()}") # Expected: 0
    print(f"After pop, min: {minStack.getMin()}") # Expected: -2

    print("\n--- Test Case 2 (Empty Stack Operations) ---")
    emptyMinStack = MinStack()
    try:
        emptyMinStack.pop() # Should handle gracefully
    except IndexError as e:
        print(e)
    try:
        print(f"Top: {emptyMinStack.top()}")
    except IndexError as e:
        print(e)
    try:
        print(f"Min: {emptyMinStack.getMin()}")
    except IndexError as e:
        print(e)

    emptyMinStack.push(5)
    print(f"After pushing 5, top: {emptyMinStack.top()}") # Expected: 5
    print(f"After pushing 5, min: {emptyMinStack.getMin()}") # Expected: 5

    print("\n--- Test Case 3 (Duplicates) ---")
    minStack3 = MinStack()
    minStack3.push(2)
    minStack3.push(0)
    minStack3.push(3)
    minStack3.push(0)
    print(f"Current top: {minStack3.top()}")   # Expected: 0
    print(f"Current min: {minStack3.getMin()}") # Expected: 0
    minStack3.pop() # pop 0
    print(f"After pop, top: {minStack3.top()}") # Expected: 3
    print(f"After pop, min: {minStack3.getMin()}") # Expected: 0 (the other 0 is still there)
    minStack3.pop() # pop 3
    print(f"After pop, top: {minStack3.top()}") # Expected: 0
    print(f"After pop, min: {minStack3.getMin()}") # Expected: 0
    minStack3.pop() # pop 0
    print(f"After pop, top: {minStack3.top()}") # Expected: 2
    print(f"After pop, min: {minStack3.getMin()}") # Expected: 2
