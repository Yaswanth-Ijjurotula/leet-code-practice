from collections import defaultdict
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach-1 (Using Hashing)
# def hasCycle(head: ListNode) -> bool:
#     h_map = defaultdict(int)
#     temp = head
#     while(temp):
#         h_map[temp]+=1
#         if h_map[temp] > 1:
#             return True
#         temp = temp.next
#     return False

# Approach-2(Using fast and slow pointers)
def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Optimal solution to find the beginning of the loop
def start_of_loop(head: ListNode):
    slow = head
    fast = head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while(slow!=fast):
                slow = slow.next
                fast = fast.next
            return slow
    return None

def len_of_loop(head: ListNode):
    slow = head
    fast = head
    len = 0
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        len += 1
        if slow == fast:
            return len
    return None
   
# Helper to create a linked list from a list and optionally create a cycle
def create_linked_list(arr, pos=-1):
    dummy = ListNode()
    curr = dummy
    nodes = []
    for val in arr:
        node = ListNode(val)
        nodes.append(node)
        curr.next = node
        curr = curr.next
    if pos != -1:
        curr.next = nodes[pos]  # Create cycle
    return dummy.next

if __name__ == "__main__":
    # Test Case 1: No cycle
    head1 = create_linked_list([3, 2, 0, -4])
    print("Test Case 1 (No cycle):", hasCycle(head1))  # Expected: False

    # Test Case 2: Cycle at position 1 (node with value 2)
    head2 = create_linked_list([3, 2, 0, -4], pos=1)
    print("Test Case 2 (Cycle at pos 1):", hasCycle(head2))  # Expected: True

    # Test Case 3: Single node, no cycle
    head3 = create_linked_list([1])
    print("Test Case 3 (Single node, no cycle):", hasCycle(head3))  # Expected: False

    # Test Case 4: Single node, cycle to itself
    head4 = create_linked_list([1], pos=0)
    print("Test Case 4 (Single node, cycle):", hasCycle(head4))  # Expected: True

    # Test Case 5: Empty list
    head5 = create_linked_list([])
    print("Test Case 5 (Empty list):", hasCycle(head5))

    # Test cases for start_of_loop
    # Test Case 1: No cycle
    head1 = create_linked_list([3, 2, 0, -4])
    print("Start of loop (No cycle):", start_of_loop(head1))  # Expected: None

    # Test Case 2: Cycle at position 1 (node with value 2)
    head2 = create_linked_list([3, 2, 0, -4], pos=1)
    loop_node = start_of_loop(head2)
    print("Start of loop (Cycle at pos 1):", loop_node.val if loop_node else None)  # Expected: 2

    # Test Case 3: Single node, no cycle
    head3 = create_linked_list([1])
    print("Start of loop (Single node, no cycle):", start_of_loop(head3))  # Expected: None

    # Test Case 4: Single node, cycle to itself
    head4 = create_linked_list([1], pos=0)
    loop_node4 = start_of_loop(head4)
    print("Start of loop (Single node, cycle):", loop_node4.val if loop_node4 else None)  # Expected: 1

    # Test Case 5: Empty list
    head5 = create_linked_list([])
    print("Start of loop (Empty list):", start_of_loop(head5))  #

    # Test cases for len_of_loop
    # Test Case 1: Cycle at position 1 (node with value 2), expected length 3
    head6 = create_linked_list([3, 2, 0, -4], pos=1)
    print("Length of loop (Cycle at pos 1):", len_of_loop(head6))  # Expected: 3

    # Test Case 2: Single node, cycle to itself, expected length 1
    head7 = create_linked_list([1], pos=0)
    print("Length of loop (Single node, cycle):", len_of_loop(head7))  # Expected: 1