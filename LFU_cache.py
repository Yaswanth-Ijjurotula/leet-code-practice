import collections

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def insert_after_head(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size +=1
    def delete_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -=1
    def get_tail_node(self):
        if self.size>0:
            return self.tail.prev
        return None
    
    class LFUcache:
        def __init__(self,capacity):
            self.capacity = capacity
            self.cache = {}
            self.freqmap = collections.defaultdict(DoublyLinkedList)
            self.min_freq = 0
        def update_frequency(self,node):
            old_freq = node.freq
            self.freqmap[old_freq].delete_node(node)
            if self.min_freq == old_freq and self.freqmap[old_freq].size == 0:
                self.min_freq += 1
            node.freq += 1
            new_freq = node.freq
            self.freqmap[new_freq].insert_after_head(node)
        def get(self,key):
            if key not in self.cache:
                return -1
            node = self.cache[key]
            self.update_frequency(node)
            return node.value
        def put(self,key,value):
            if self.capacity == 0:
                return
            if key in self.cache:
                node = self.cache[key]
                node.value = value
                self.update_frequency(node)
                return
            if len(self.cache) == self.capacity:
                lfu_list = self.freqmap[self.min_freq]
                lfu_node = lfu_list.get_tail_node()
                if lfu_node:
                    self.remove_from_cache(lfu_node)
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.freqmap[1].insert_after_head(new_node)
            self.min_freq = 1


        def remove_from_cache(self,node):
            self.freqmap[node.freq].delete_node(node)
            del self.cache[node.key]