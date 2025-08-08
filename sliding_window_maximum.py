import collections

class Solution:
    # Brute force

    # def maxSlidingWindow(self, nums, k):
    #     n = len(nums)
    #     result = []
    #     for i in range(n):
    #         m = float('-inf')
    #         x = i 
    #         j = i+k-1
    #         if j == n:
    #             break
    #         while(x <= j):
    #             m = max(nums[x],m)
    #             x +=1
    #         result.append(m)
    #     return result
            
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if n == 0 or k == 0:
            return []
        dq = collections.deque()
        res = []
        for i in range(n):
            if dq and dq[0] == i-k: 
                dq.popleft() #pop from the front when the deque exceeds the capacity or window  size
            while  dq and nums[dq[-1]] <= nums[i]:
                dq.pop() #popping all the elements from the back, if element at the back is lesser than the current element in the window.
            dq.append(i)
            if i >= k-1:
                res.append(nums[dq[0]]) #maximum element is always at the front of the deque as we are popping from the back.
        return res

# --- Example Usage (for testing purposes) ---
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Standard example
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    expected1 = [3, 3, 5, 5, 6, 7]
    result1 = sol.maxSlidingWindow(nums1, k1)
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {result1}")
    print(f"Expected: {expected1}")
    print(f"Match: {result1 == expected1}\n")

    # Test Case 2: Simple example
    nums2 = [1, 2, 3, 4, 5]
    k2 = 2
    expected2 = [2, 3, 4, 5]
    result2 = sol.maxSlidingWindow(nums2, k2)
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {result2}")
    print(f"Expected: {expected2}")
    print(f"Match: {result2 == expected2}\n")

    # Test Case 3: Decreasing numbers
    nums3 = [5, 4, 3, 2, 1]
    k3 = 3
    expected3 = [5, 4, 3]
    result3 = sol.maxSlidingWindow(nums3, k3)
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {result3}")
    print(f"Expected: {expected3}")
    print(f"Match: {result3 == expected3}\n")
    
    # Test Case 4: Single element window
    nums4 = [10, 5, 2, 7, 8, 3]
    k4 = 1
    expected4 = [10, 5, 2, 7, 8, 3]
    result4 = sol.maxSlidingWindow(nums4, k4)
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Output: {result4}")
    print(f"Expected: {expected4}")
    print(f"Match: {result4 == expected4}\n")