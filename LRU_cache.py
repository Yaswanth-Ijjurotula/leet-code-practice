class Node:
    def __init__(self,key1,value1,next1=None,back1=None):
        self.key = key1
        self.value = value1
        self.next = next1
        self.back = back1
    

class LRUCache:
    head = Node(0,0), tail = Node(0,0)
    def __init__(self,capacity1):
         self.cache = {}
         self.capacity = capacity1
         self.head.next = self.tail
         self.tail.back = self.head
    def deleteNode(self,node):
        node.back.next = node.next
        node.next.back = node.back
        del self.cache[node.key]
    def insert(self,node):
        self.cache[node.key] = node
        front = self.head.next
        self.head.next = node 
        node.next = front
        node.back = self.head
        front.back = node
    def put(self,key,value):
        if key in self.cache:
            self.deleteNode(self.cache[key])
        if len(self.cache) == self.capacity:
            self.deleteNode(self.tail.back)
        self.insert(Node(key,value))
    def get(self,key):
        value = -1
        if key in self.cache:
            value = self.cache[key].value
            self.deleteNode(self.cache[key])
            self.insert(Node(key,value))
        return value
            





