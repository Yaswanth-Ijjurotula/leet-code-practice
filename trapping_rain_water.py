# Approach - 1 (TC: O(3N)~O(N,SC: 2N)
# def trap(height):
#     prefix = [0]*len(height)
#     suffix = [0]*len(height)
#     max = 0
#     max2 = 0
#     sum = 0
#     for i in range(len(height)):
#         if height[i]> max:
#             max = height[i]
#         prefix[i] = max
#     for j in range(len(height)-1,-1,-1):
#         if height[j]> max2:
#             max2 = height[j]
#         suffix[j] = max2
#     for i in range(len(height)):
#         sum = sum + (min(prefix[i],suffix[i]) - height[i])
#     return sum

#Approach - 2 - Monotonic stack 
# def trap(height):
#     stack = []
#     trapped_water = 0
#     for i in range(len(height)):
#         while(stack and height[i] > height[stack[-1]]): 
#             top = stack.pop()
#             if not stack:
#                 break
#             h= min(height[i],height[(stack[-1])]) - height[top]
#             w =  i - stack[-1]-1
#             trapped_water = trapped_water + (h * w)
#         stack.append(i)
#     return trapped_water

def trap(height):
    n = len(height)
    left = 0
    right = n-1
    res = 0
    maxLeft = 0
    maxRight = 0
    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= maxLeft:
                maxLeft = height[left]
            else:
                res += maxLeft - height[left]
            left += 1
        else:
            if height[right] >= maxRight:
                maxRight = height[right]
            else:
                res += maxRight - height[right]
            right -= 1
    return res

        
    
    
        
if __name__ == "__main__":
    # Example 1
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print("Example 1:", trap(height1))  # Expected: 6

    # Example 2
    height2 = [4,2,0,3,2,5]
    print("Example 2:", trap(height2))  # Expected: 9

    # Example 3: No bars
    height3 = []
    print("Example 3:", trap(height3))  # Expected: 0

    # Example 4: All bars same height
    height4 = [2,2,2,2]
    print("Example 4:", trap(height4))  # Expected: