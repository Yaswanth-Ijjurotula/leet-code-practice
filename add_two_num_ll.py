class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next                

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    temp = dummy
    carry = 0
    result = []
    while(l1 or l2 or carry):
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = int(sum/10)
            temp.next = ListNode(int(sum%10))
            temp = temp.next         
    return dummy.next

                 
def list_to_linkedlist(l):
    head = ListNode(l[0])
    temp = head
    for i in range(1,len(l)):
        temp.next = ListNode(l[i])
        temp = temp.next
    return head

def printLL(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next

if __name__ == "__main__":
    # Example usage:
    l1 = list_to_linkedlist([2,4,3])  # represents 342
    l2 = list_to_linkedlist([5,6,4])  # represents 465
    result = addTwoNumbers(l1, l2)
    printLL(result)

    


