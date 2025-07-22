import collections

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# def sort_stack(s: Stack) -> Stack:
    # temp = Stack()
    # while not s.is_empty():
    #     if temp.is_empty():
    #         temp.push(s.pop())
    #         continue
    #     elif s.peek() < temp.peek():
    #         ele_to_insert = s.pop()
    #         while(not temp.is_empty() and ele_to_insert < temp.peek()):
    #             s.push(temp.pop())
    #         temp.push(ele_to_insert)
    #     else:
    #         temp.push(s.pop())
    # return temp

def sort_stack(s: Stack) -> Stack:
    if s.is_empty():
        return 
    temp = s.pop()
    sort_stack(s)
    insert_at_right_position(s,temp)
    return s

    
def insert_at_right_position(s,temp):
    if s.is_empty() or temp >= s.peek():
        s.push(temp)
        return
    else:
        ele = s.pop()
        insert_at_right_position(s,temp)
        s.push(ele)
    return 


# --- Example Usage ---
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(34)
    my_stack.push(3)
    my_stack.push(31)
    my_stack.push(98)
    my_stack.push(92)
    my_stack.push(23)

    print(f"Original stack: {my_stack}")

    sorted_result_stack = sort_stack(my_stack)
    print(f"Sorted stack (smallest on top): {sorted_result_stack}")

    # You can also test with an empty stack or a stack with one element
    empty_stack = Stack()
    print(f"Original empty stack: {empty_stack}")
    sorted_empty_stack = sort_stack(empty_stack)
    print(f"Sorted empty stack: {sorted_empty_stack}")

    single_element_stack = Stack()
    single_element_stack.push(10)
    print(f"Original single element stack: {single_element_stack}")
    sorted_single_element_stack = sort_stack(single_element_stack)
    print(f"Sorted single element stack: {sorted_single_element_stack}")