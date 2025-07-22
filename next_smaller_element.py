def next_smaller_element(nums):
    n = len(nums)
    nse = [-1]*n
    stack = []
    for i in range(n-1,-1,-1):
        while stack and nums[i] <= stack[-1]:
            stack.pop()
        if stack:
            nse[i] = stack[-1]
        stack.append(nums[i])
    return nse
        
        
   

if __name__ == "__main__":
    # Example 1
    nums1 = [4, 5, 2, 10, 8]
    print("Example 1:", next_smaller_element(nums1))  

    # Example 2
    nums2 = [4, 8, 5, 2, 25]
    print("Example 2:", next_smaller_element(nums2))  

    # Example 3: All decreasing
    nums3 = [5, 4, 3, 2, 1]
    print("Example 3:", next_smaller_element(nums3))  

    # Example 4: