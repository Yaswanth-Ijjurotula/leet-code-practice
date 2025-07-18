class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        temp = dummy
        while(list1 and list2):
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
                temp.next = list1
        else:
                temp.next = list2
                
        return dummy.next

def print_linkedlist(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

# Example usage:
if __name__ == "__main__":
    # Helper to create linked list from list
    def list_to_linkedlist(lst):
        dummy = ListNode()
        curr = dummy
        for num in lst:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

    l1 = list_to_linkedlist([1,2,4])
    l2 = list_to_linkedlist([1,3,4])
    s = Solution()
    merged_head = s.mergeTwoLists(l1, l2)
    print_linkedlist(merged_head)  # Output: 1 1 2 3 4 4


