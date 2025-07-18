class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: ListNode, k: int) -> ListNode:
    if(head == None):
        return None
    temp = head
    fast = head
    slow = head
    count = 0
    while(temp):
        count+=1
        temp = temp.next
    k = k%count
    while(k):
        if fast.next:
            fast = fast.next
            k -= 1
        else:
            fast = head
            k -= 1
    while fast.next:
        fast = fast.next
        slow = slow.next
    fast.next = head
    head = slow.next
    slow.next = None
    return head
       

# Helper to create a linked list from a list
def create_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper to print a linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

if __name__ == "__main__":
    # Example 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = rotateRight(head1, 2)
    print("Example 1:")
    print_linked_list(result1)  # Expected: 4 -> 5 -> 1 -> 2 -> 3 -> None

    # Example 2
    head2 = create_linked_list([0, 1, 2])
    result2 = rotateRight(head2, 4)
    print("Example 2:")
    print_linked_list(result2)  # Expected: 2 -> 0 -> 1 -> None

    # Example 3: Empty list
    head3 = create_linked_list([])
    result3 = rotateRight(head3, 1)
    print("Example 3:")
    print_linked_list(result3)  # Expected: None