class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_ll(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_ll(head.next)
    head.next.next = head
    head.next = None
    return new_head

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = head
    count = 0
    prev = None
    while (dummy):
        count+=1
        if count%k == 0:
            front = dummy.next
            dummy.next = None
            if count == k:
                main_head = reverse_ll(head)
            else:
                new_head = reverse_ll(head)
                prev.next = new_head
            prev = head
            head.next = front
            head = head.next
            dummy = prev
        dummy = dummy.next
    if count < k:
        return head
    return main_head
                
            

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
    # Example 1: k = 2
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = reverseKGroup(head1, 2)
    print("Example 1 (k=2):")
    print_linked_list(result1)  # Expected: 2 -> 1 -> 4 -> 3 -> 5 -> None

    # Example 2: k = 3
    head2 = create_linked_list([1, 2, 3, 4, 5])
    result2 = reverseKGroup(head2, 3)
    print("Example 2 (k=3):")
    print_linked_list(result2)  # Expected: 3 -> 2 -> 1 -> 4 -> 5 -> None

    # Example 3: k = 1 (no change)
    head3 = create_linked_list([1, 2, 3])
    result3 = reverseKGroup(head3, 1)
    print("Example 3 (k=1):")
    print_linked_list(result3)  # Expected: 1 -> 2 -> 3 -> None

    # Example 4: k greater than list length (no change)
    head4 = create_linked_list([1, 2])
    result4 = reverseKGroup(head4, 3)
    print("Example 4 (k=3):")
    print_linked_list(result4)  # Expected: 1 -> 2 -> None