class Node:
    def __init__(self,data1,next1=None):
        self.data = data1
        self.next = next1

def printLL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next

def reverse(head):
    # BF Approach
    # current = head
    # stack = []
    # while(current):
    #     stack.append(current.data)
    #     current = current.next
    # current = head
    # while(current):
    #     current.data = stack.pop()
    #     current = current.next
    # return head

    # Optimal Approach
    # prev = None
    # current = head
    # while current:
    #     next_node = current.next    
    #     current.next = prev         
    #     prev = current             
    #     current = next_node        
    # return prev                

    # Optimal Approach using recursion
    if head is None or head.next is None:
        return head
    new_head = reverse(head.next)  
    front = head.next
    front.next = head
    head.next = None
    return new_head
    

if __name__ == "__main__":
    # Sample array and value for insertion
    arr = [12, 8, 5, 7]
    head = Node(arr[0])
    current_node = head
    for i in range(1,len(arr)):
        if current_node:
            current_node.next = Node(arr[i])
            current_node = current_node.next
    printLL(head)
    print()
    head = reverse(head)
    printLL(head)