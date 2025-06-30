from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       #BF Approach - N^2
    #    my_dict = {}
    #    for i in nums:
    #        if i not in my_dict:
    #            my_dict[i] = 1
    #        else:
    #            return i
               
   
    #Optimal Approach - Floyd's Algorithm
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            print(slow)
        return slow

# Example Calls:
if __name__ == "__main__":
    # Example 1
    nums1 = [1, 3, 4, 2, 2]
    solver1 = Solution()
    duplicate1 = solver1.findDuplicate(nums1)
    print(f"Input: {nums1}, Duplicate: {duplicate1}") # Expected output: 2

    # Example 2
    nums2 = [3, 1, 3, 4, 2]
    solver2 = Solution()
    duplicate2 = solver2.findDuplicate(nums2)
    print(f"Input: {nums2}, Duplicate: {duplicate2}") # Expected output: 3