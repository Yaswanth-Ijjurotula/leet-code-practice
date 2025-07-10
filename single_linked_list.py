# Node class to represent a linked list node
class Node:
    def __init__(self,data1,next1=None):
        self.data= data1
        self.next = next1

# Function to print Linked List
def printLL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    
# Function to insert value at the head of Linked List
def insertHead(head,val):
    temp = Node(val,head)
    return temp

# Function to delete a node at the tail of the Linked List
def deleteTail(head):
    if head is None or head.next is None:
        return None
    current_node = head
    while(current_node.next):
        if current_node.next.next == None:
            current_node.next = None
        else:
            current_node = current_node.next

# Function to find the length of the Linked ist
def findLen(head):
    temp = head
    count = 0
    while(temp):
        count+=1
        temp = temp.next
    return count
# Function to search value in a Linked list
def lin_search(head,val):
    temp = head
    while(temp):
        if temp.data == val:
            return True
        temp = temp.next
    return False


if __name__ == "__main__":
    # Sample array and value for insertion
    arr = [12, 8, 5, 7]
    val = 100

    # Creating a linked list with initial elements from the array- hardcoding
    # head = Node(arr[0])
    # head.next = Node(arr[1])
    # head.next.next = Node(arr[2])
    # head.next.next.next = Node(arr[3])

    head = Node(arr[0])
    current_node = head
    for i in range(1,len(arr)):
        if current_node:
            current_node.next = Node(arr[i])
            current_node = current_node.next
    
    # Printing the length of the Linked List
    len = findLen(head)
    print(len)


    #Inserting a new node at the head of the linked list
    head = insertHead(head, val)

    # Printing the linked list
    print("Linked List after insertion (if any):")
    printLL(head)
    print()  # For a newline after printing the list

    # Printing the length of the Linked List after insertion
    len = findLen(head)
    print(len)

    # Printing the linked list after deleting the tail
    deleteTail(head)
    printLL(head)
    print()

    # Printing the length of the Linked List after deletion
    len = findLen(head)
    print(len)
    print()

    # Printing True or False,based on whether the element is present or not
    v = 8
    print(lin_search(head,v))
