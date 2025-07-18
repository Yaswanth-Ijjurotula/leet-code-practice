class Node:
    def __init__(self,data1,next1 = None):
        self.data = data1
        self.next = next1
# Approach to get the intersection value only.   
# def reverse_ll(head):
#     current = head
#     prev = None
#     while current:
#         front = current.next
#         current.next = prev
#         prev = current
#         current = front
#     return prev
    
# def find_intersection(l1,l2):
#     temp1 = reverse_ll(l1)
#     temp2 = reverse_ll(l2)
#     intersect = None
#     if temp1.data != temp2.data:
#         return intersect
#     while(temp1 and temp2):
#         if temp1.data == temp2.data:
#             intersect = temp1.data
#             temp1 = temp1.next
#             temp2 = temp2.next
#         else:
#             break
#     return intersect

# Approach - 1(O(2M))
# def difference(head1,head2):
#     len1 = 0
#     len2 = 0
#     while(head1 or head2):
#         if head1:
#             len1+=1
#             head1 = head1.next
#         if head2:
#             len2+=1
#             head2 = head2.next
#     return len1-len2
# def find_intersection(l1,l2):
#     skip = difference(l1,l2)
#     temp1 = l1
#     temp2 = l2
#     intersect = None
#     if skip > 0:
#         while(skip):
#             temp1 = temp1.next
#             skip -= 1
#     else:
#         while(skip != 0):
#             temp2 = temp2.next
#             skip += 1
#     print(temp2.data)
#     while temp1 and temp2:
#         if temp1 == temp2:
#             return temp1.data
#         else:
#             temp1 = temp1.next
#             temp2 = temp2.next
#     return None

# Approach-2(O(2M))
def find_intersection(l1,l2):
    temp1 = l1
    temp2 = l2
    while (temp1 != temp2):
        if temp1!= None and temp2!=None:
            temp1 = temp1.next
            temp2 = temp2.next
        elif temp1 == None:
            temp1 = l2
        else:
            temp2 = l1
    if temp1 == None:
        return None
    return temp1.data




if __name__ == "__main__":
    # Helper to print a linked list (for debugging)
    def print_ll(head):
        while head:
            print(head.data, end=" -> ")
            head = head.next
        print("None")

    # Test Case 1: Intersection at tail (node with value 4)
    common = Node(4)
    l1 = Node(1, Node(3, Node(1, Node(2, common))))
    l2 = Node(3, Node(2, common))
    intersection_point = find_intersection(l1, l2)
    print("Test Case 1 Intersection:", intersection_point)  # Expected: 4

    # Test Case 2: No intersection
    l3 = Node(1, Node(2, Node(3)))
    l4 = Node(4, Node(5, Node(6)))
    intersection_point2 = find_intersection(l3, l4)
    print("Test Case 2 Intersection:", intersection_point2)  # Expected: None

    # Test Case 3: Complete overlap (identical lists, same reference)
    l5 = Node(7, Node(8, Node(9)))
    l6 = l5  # Both point to the same list
    intersection_point3 = find_intersection(l5, l6)
    print("Test Case 3 Intersection:", intersection_point3)  # Expected: 7

    # Test Case 4: Intersection at head (both lists are the same object)
    l7 = Node(10, Node(20, Node(30)))
    l8 = l7
    intersection_point4 = find_intersection(l7, l8)
    print("Test Case 4 Intersection:", intersection_point4)  # Expected: 10

    # Test Case 5: One list is a subset/tail of the other (intersection at 7)
    tail = Node(7, Node(8))
    l9 = Node(5, Node(6, tail))
    l10 = tail
    intersection_point5 = find_intersection(l9, l10)
    print("Test Case 5 Intersection:", intersection_point5)  # Expected: 7