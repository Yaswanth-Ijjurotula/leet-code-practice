# Assume your Solution class and its longestConsecutive method are defined.
# For example:
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Better approch(O(N)+ O(nlogn)for sort), works with arrays without duplicates
        # n = len(nums)
        # if n == 0:
        #     return 0
        # max_window = 1
        # nums.sort()
        # l =  0 
        # r = l+1
        # while(l < r and r < n):
        #     if(nums[r] == nums[r-1]+1):
        #         temp = r-l+1
        #         if(max_window < temp):
        #             max_window = temp
        #         r += 1

        #     else:
        #         l = r
        #         r += 1
        # return max_window

        # Optimal Approach- O(nlogn) - handles duplicates 
        # n = len(nums)
        # if n == 0:
        #     return 0
        # nums.sort()
        # crnt = 1
        # longest = 1
        # for i in range(n-1):
        #     if(nums[i] == nums[i+1]-1):
        #         crnt+=1
        #         # print(crnt)
        #     elif(nums[i] == nums[i+1]):
        #         continue
        #     else:
        #         crnt = 1
        #     longest = max(crnt,longest)
        #     # print("#",longest)
        # return longest
        
        # Optimal Approach - 2 -> O(2N)
        n = len(nums)
        if n == 0:
            return 0
        longest = 1
        st = set(nums)
        for item in st:
            if item-1 not in st:
                x = item
                cnt = 1
                while x+1 in st:
                    x = x+1
                    cnt +=1
                longest = max(cnt,longest)
        return longest


if __name__ == "__main__":
    # Create an instance of the Solution class to call the method
    solver = Solution()

    # Example 1
    nums1 = [100, 200, 1, 3, 2, 4]
    result1 = solver.longestConsecutive(nums1)
    print(f"Input: {nums1}, Output: {result1} (Expected: 4)")

    # Example 2
    nums2 = [3, 8, 5, 7, 6]
    result2 = solver.longestConsecutive(nums2)
    print(f"Input: {nums2}, Output: {result2} (Expected: 4)")

    # Additional common test cases
    nums3 = [] # Empty array
    result3 = solver.longestConsecutive(nums3)
    print(f"Input: {nums3}, Output: {result3} (Expected: 0)")

    nums4 = [5] # Single element array
    result4 = solver.longestConsecutive(nums4)
    print(f"Input: {nums4}, Output: {result4} (Expected: 1)")

    nums5 = [1, 2, 0, 1] # Duplicates and zero
    result5 = solver.longestConsecutive(nums5)
    print(f"Input: {nums5}, Output: {result5} (Expected: 3)") # Sequence: 0, 1, 2

    
    nums6 = [9,1,4,7,3,-1,0,5,8,-1,6] 
    result6 = solver.longestConsecutive(nums6)
    print(f"Input: {nums6}, Output: {result6} (Expected: 7)") 