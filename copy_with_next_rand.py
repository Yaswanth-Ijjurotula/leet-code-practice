class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
# Bruteforce Approach - TC - O(N), SC - O(N)
# def copyRandomList(head: 'Node') -> 'Node':
#         temp = head
#         copy_map = {}
#         if head == None:
#             return None
#         while(temp):
#             copy_map[temp] = Node(temp.val)
#             temp = temp.next
#         temp = head
#         copy_head= copy_map[temp]
#         temp1 = copy_head
#         while(temp):
#             if temp.random == None:
#                 temp1.random = None
#             else:
#                 temp1.random = copy_map[temp.random]
#             if temp.next == None:
#                 temp1.next = None
#                 break
#             temp1.next = copy_map[temp.next]
#             temp = temp.next
#             temp1 = temp1.next
#         return copy_head

# Optimal Approach -
def copyRandomList(head: 'Node') -> 'Node':
    temp = head
    if head == None:
        return None
    while(temp):
        front = temp.next
        temp.next = Node(temp.val)
        temp.next.next = front
        temp = temp.next.next
    temp = head
    while(temp):
        clone = temp.next
        if temp.random ==None:
            clone.random = None
        else:
            clone.random = temp.random.next
            print(clone.random.val)
        temp = clone.next
    temp = head
    dummy = Node(-1)
    temp1 = dummy
    while(temp):
        temp1.next = temp.next
        temp.next = temp.next.next
        temp1 = temp1.next
        temp = temp.next
    return dummy.next
# Helper to create a linked list from a list of (val, random_index) tuples
def create_linked_list_with_random(arr):
    if not arr:
        return None
    nodes = [Node(val) for val, _ in arr]
    for i, (val, rand_idx) in enumerate(arr):
        if i < len(arr) - 1:
            nodes[i].next = nodes[i+1]
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]

# Helper to print a linked list with random pointers
def print_linked_list_with_random(head):
    curr = head
    nodes = []
    while curr:
        rand_val = curr.random.val if curr.random else None
        nodes.append(f"({curr.val}, rand:{rand_val})")
        curr = curr.next
    print(" -> ".join(nodes))

if __name__ == "__main__":
    # Example 1: 1 -> 2 -> 3, randoms: 1->3, 2->1, 3->2
    arr1 = [(1, 2), (2, 0), (3, 1)]
    head1 = create_linked_list_with_random(arr1)
    print("Original list:")
    print_linked_list_with_random(head1)
    cloned1 = copyRandomList(head1)
    print("Cloned list:")
    print_linked_list_with_random(cloned1)

    # Example 2: Empty list
    head2 = create_linked_list_with_random([])
    print("Original list (empty):")
    print_linked_list_with_random(head2)
    cloned2 = copyRandomList(head2)
    print("Cloned list (empty):")