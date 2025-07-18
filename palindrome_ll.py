class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Bruteforce Approach - TC-O(N),SC-O(1)
# def isPalindrome(head: ListNode) -> bool:
#     stack = []
#     dummy = head
#     if dummy == None:
#         return False
#     while(dummy):
#         stack.append(dummy.val)
#         dummy = dummy.next
#     dummy = head
#     while(dummy):
#         ele = stack.pop()
#         if dummy.val != ele:
#             return False
#         dummy = dummy.next
#     return True

# Optimal Approach 
def reverse_ll(head):
    prev = None
    current = head
    print(current.val)
    while(current):
        front = current.next
        current.next = prev
        prev = current
        current = front
    return prev
def isPalindrome(head: ListNode) -> bool:
    slow = head
    fast = head
    if slow == None or slow.next == None:
       return True
    while(fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
    first = head
    second = reverse_ll(slow.next)
    while second:
        if first.val == second.val:
            first = first.next
            second = second.next
        else:
            return False
    reverse_ll(second)
    return True
    
    
   

# Helper to create a linked list from a list
def create_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    # Test Case 1: Palindrome
    head1 = create_linked_list([1, 2, 2, 1])
    print("Test Case 1:", isPalindrome(head1))  # Expected: True

    # Test Case 2: Not a palindrome
    head2 = create_linked_list([1, 2])
    print("Test Case 2:", isPalindrome(head2))  # Expected: False

    # Test Case 3: Single node
    head3 = create_linked_list([1])
    print("Test Case 3:", isPalindrome(head3))  # Expected: True

    # Test Case 4: Empty list
    head4 = create_linked_list([])
    print("Test Case 4:", isPalindrome(head4))  #