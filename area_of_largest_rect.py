from typing import List
# def largestRectangleArea(heights: List[int]) -> int:
#     stack = []
#     max_area = 0
#     left_small = [0]*len(heights)
#     right_small = [0]*len(heights)
#     for i in range(len(heights)):
#         while stack and heights[stack[-1]] >= heights[i]:
#             stack.pop()
#         if not stack:
#            left_small[i] = 0
#         else:
#             left_small[i] = stack[-1]+1
#         stack.append(i)
#     stack.clear()
#     for i in range(len(heights)-1,-1,-1):
#         while stack and heights[stack[-1]] >= heights[i]:
#             stack.pop()
#         if not stack:
#            right_small[i] = len(heights)-1
#         else:
#             right_small[i] = stack[-1]-1
#         stack.append(i)
#     for i in range(len(heights)):
#         a = (right_small[i] - left_small[i] + 1)* heights[i]
#         max_area = max(a,max_area)
#     return max_area

# Optimal Approach(one pass)
def largestRectangleArea(heights: List[int]) -> int:
    stack = [] #[index,height]
    max_area = 0
    for i in range(len(heights)):
        start = i
        while stack and stack[-1][1] > heights[i]:
            ind,h = stack.pop()
            max_area = max((i-ind)*h,max_area)
            start = ind
        stack.append([start,heights[i]])
    for j,h in stack:
        max_area = max(max_area,h*(len(heights)-j))
    return max_area

 
    



       
# --- Example Usage ---
if __name__ == "__main__":
    # Test case: Heights of the histogram bars
    hist_heights = [2, 1, 5, 6, 2, 3]
    
    print(f"Heights: {hist_heights}")
    
    # Calculate the largest area
    result = largestRectangleArea(hist_heights)
    
    # The largest rectangle is formed by bars 5 and 6 (height 5, width 2), area = 10.
    print(f"Largest rectangle area: {result}") # Expected output: 10

    # Another test case
    hist_heights_2 = [2, 4]
    print(f"\nHeights: {hist_heights_2}")
    result_2 = largestRectangleArea(hist_heights_2)
    print(f"Largest rectangle area: {result_2}") # Expected output: 4