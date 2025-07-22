class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.count = 0
        self.n = 5
        self.arr = [0]*self.n
    def push(self,x):
        if self.count == self.n:
            return -1
        else:
            self.arr[self.rear%self.n] = x
            self.rear += 1 
            self.count += 1
    def pop(self):
        if self.count == 0:
            return -1
        self.count -= 1
        ele = self.arr[self.front%self.n]
        self.front += 1
        return ele
    def Top(self):
        if self.count == 0:
            return -1
        return self.arr[self.front%self.n]
    def Size(self):
        return self.count
    
if __name__ == "__main__":
    q = Queue()
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.Top())
    print("The size of the queue before deletion", q.Size())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.Top())
    print("The size of the queue after deleting an element", q.Size())
        