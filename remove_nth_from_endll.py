class Node:
    def __init__(self,data1,next1=None):
        self.data = data1
        self.next = next1
def printLL(head):
    temp = head
    while (temp):
        print(temp.data,end= " ")
        temp = temp.next

def remove_n_element(head,n):
    # BF Approach
    # temp = head
    # count = 0
    # while(temp):
    #     count += 1
    #     temp = temp.next
    # if count <= 1:
    #     return 
    # ele = count - n 
    # temp = head
    # prev = None
    # front = temp.next
    # while(ele):
    #     prev = temp
    #     temp = temp.next
    #     front = temp.next
    #     ele -=1
    # if prev != None:
    #     prev.next = front
    # else:
    #     head = temp.next
    # return head

    # Optimal Approach
    fast = head
    slow = head
    for i in range(n):
        fast = fast.next
    if fast == None:
        return head.next
    while(fast.next != None):
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head

    

if __name__ == "__main__":
    ll = [1,2]
    head = Node(ll[0])
    current = head
    for i in range(1,len(ll)):
        current.next = Node(ll[i])
        current = current.next
    printLL(head)
    n = 2
    head = remove_n_element(head,n)
    print("After deletion")
    printLL(head)
