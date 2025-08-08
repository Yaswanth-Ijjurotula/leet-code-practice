import collections

_knows_matrix = [
    [False, False, True, False],  
    [False, False, True, False],  
    [False, False, False, False], 
    [False, False, True, False]   
]

def knows(a, b):
    n = len(_knows_matrix)
    if 0 <= a < n and 0 <= b < n:
        return _knows_matrix[a][b]
    return False

def find_celebrity(n):
    # Bruteforce approach - O(N2)

    # know_me = [0]*n
    # i_know = [0]*n
    # for i in range(n):
    #     for j in range(n):
    #         if knows(i,j) and i != j:
    #             i_know[i] += 1
    #         if knows(j,i) and j != i:
    #             know_me[i]+=1
    # for i in range(n):
    #     if i_know[i] == 0 and know_me[i] == n-1:
    #         return i
    # return -1

    # Approach - 2 - Two pointer approach
    # top = 0
    # bottom = n-1
    # while top < bottom:
    #     if knows(top,bottom):
    #         top += 1
    #     elif knows(bottom,top):
    #         bottom -= 1
    #     else:
    #         top += 1
    #         bottom -= 1
    # if top == bottom: 
    #     for i in range(n):
    #         if i == top:
    #             continue
    #         if not knows(top,i) and knows(i,top):
    #             continue
    #         else:
    #             return -1
    # else:
    #     return -1
    # return top
    
    # Approach - 2(optimized)
    # if n <= 1:
    #     return 0 if n == 1 else -1
    # top = 0
    # bottom = n - 1
    # while top < bottom:
    #     if knows(top, bottom):
    #         # If 'top' knows 'bottom', then 'top' cannot be the celebrity.
    #         # We eliminate 'top' and move to the next person.
    #         top += 1
    #     else:
    #         # If 'top' does NOT know 'bottom', then 'bottom' cannot be the celebrity
    #         # (because a celebrity must be known by everyone).
    #         # We eliminate 'bottom' and move the pointer back.
    #         bottom -= 1
    # candidate = top
    # for i in range(n):
    #     if i != candidate:
    #         if knows(candidate, i):
    #             return -1  
    #         if not knows(i, candidate):
    #             return -1  
    # return candidate

    # Approach-3 (using stack)
    if n <= 1:
        return 0 if n == 1 else -1
    stack = list(range(n))
    while(len(stack)> 1):
        a = stack.pop()
        b = stack.pop()
        if knows(a,b):
            stack.append(b)
        else:
            stack.append(a)
    celebrity = stack[0]
    for i in range(n):
        if celebrity != i:
            if knows(celebrity,i) or not knows(i,celebrity):
                return -1
    return celebrity

        


# Main function to run the example
if __name__ == "__main__":
    n = 4  # Number of people
    celebrity = find_celebrity(n)

    if celebrity == -1:
        print("No celebrity found.")
    else:
        print(f"The celebrity is person {celebrity}.")