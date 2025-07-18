class Node:
    def __init__(self, val, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

def merge_lists(l1,l2):
    dummy = Node(-1)
    temp = dummy
    while(l1 != None and l2 != None):
        if (l1.val <= l2.val):
            temp.child = l1
            temp = l1
            l1 = l1.child
        else:
            temp.child = l2
            temp = l2
            l2 = l2.child
        temp.next = None
    if l1:
        temp.child = l1
    if l2:
        temp.child = l2
    if dummy.child:
        dummy.child.next = None
    return dummy.child

def flatten(head: 'Node') -> 'Node':
    if head == None or head.next == None:
        return head
    sec_head = flatten(head.next)
    head = merge_lists(head,sec_head)
    return head


# Print the linked list by traversing through child pointers
def printLinkedList(head):
    while head:
        print(head.val, end=" ")
        head = head.child
    print()

# Print the linked list in a grid-like structure
def printOriginalLinkedList(head, depth):
    while head:
        print(head.val, end="")
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)
        if head.next:
            print()
            print("| " * depth, end="")
        head = head.next

if __name__ == "__main__":
    # Example 1: Provided complex structure
    head = Node(5)
    head.child = Node(14)
    head.next = Node(10)
    head.next.child = Node(4)
    head.next.next = Node(12)
    head.next.next.child = Node(20)
    head.next.next.child.child = Node(13)
    head.next.next.next = Node(7)
    head.next.next.next.child = Node(17)

    print("Original linked list:")
    printOriginalLinkedList(head, 0)
    print("\nFlattened linked list:")
    flat = flatten(head)
    printLinkedList(flat)  # Expected: 4 5 7 10 12 13 14 17 20