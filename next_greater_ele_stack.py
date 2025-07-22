def next_greater_elements(nums):
    n = len(nums)
    st = []
    nge = [-1]*n
    for i in range(2 * (n-1),-1,-1):
        while st and st[-1] <= nums[i%n]:
           st.pop()
        if i<n and st:
            nge[i] = st[-1]
        st.append(nums[i%n])
    return nge
           
        
   

if __name__ == "__main__":
    # Example 1
    nums1 = [4, 5, 2, 10, 8]
    print("Example 1:", next_greater_elements(nums1))  # Expected: [5, 10, 10, -1, -1]

    # Example 2
    nums2 = [1, 3, 2, 4]
    print("Example 2:", next_greater_elements(nums2))  # Expected: [3, 4, 4, -1]

    # Example 3: All decreasing
    nums3 = [5, 4, 3, 2, 1]
    print("Example 3:", next_greater_elements(nums3))  # Expected: [-1, -1, -1, -1, -1]

    # Example 4: