class Node:
    def __init__(self,val1,next1 = None):
        self.val = val1
        self.next = next1
class Solution:
    # Function to print Linked List
    def printLL(self,head):
        temp = head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
    def getNode(self,head: Node, n: int):
        while head.val != n:
            head = head.next
        return head

    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

if __name__ == "__main__":
    ll = [4,5,1,9]
    head = Node(ll[0])
    current = head
    for i in range(1,len(ll)):
        current.next = Node(ll[i])
        current = current.next
    s = Solution()
    s.printLL(head)
    node = s.getNode(head,1)
    s.deleteNode(node)
    print("After deletion")
    s.printLL(head)
