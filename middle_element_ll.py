class Node:
    def __init__(self,data1,next1 = None):
        self.data = data1
        self.next = next1
    
# Function to print Linked List
def printLL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next

def find_middle(head):
    # Approach-1
    # temp = head
    # cnt = 0
    # while(temp):
    #     cnt += 1
    #     temp = temp.next
    # temp = head
    # ele = (cnt//2)+1
    # while(ele):
    #     mid = temp.data
    #     temp = temp.next
    #     ele -= 1
    # return mid

    # Approach-2 - using Tortoise and Hare algorithm
    slow = head
    fast = head
    while(fast and fast.next and slow):
        slow = slow.next
        fast = fast.next.next
    return slow.data

    



if __name__ == "__main__":
    arr = [12, 8, 5, 7]
    head = Node(arr[0])
    current = head
    for i in range(1,len(arr)):
        if current:
            current.next = Node(arr[i])
            current = current.next
    printLL(head)
    print()
    mid = find_middle(head)
    print(mid)
   