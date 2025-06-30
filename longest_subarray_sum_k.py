from typing import List

class Solution:
    def longestSubarrayWithSumZero(self, nums: List[int]) -> int:
       #BF Approach
        # st_index = 0
        # end_index = 0
        # current_length = 0
        # max_length = 0
        # k = 0
        # for i in range(len(nums)):
        #     sum=nums[i]
        #     for j in range(i+1,len(nums)):
        #        sum = sum + nums[j]
        #        if sum == k:
        #            start_index = i
        #            end_index = j
        #            current_length = j-i+1
        #            max_length = max(current_length,max_length) 
        # return max_length

        # Optimal Approach
        prefix_sum = {}
        sum = 0
        max_length = 0
        crnt_length = 0
        for i in range(len(nums)):
            sum = sum+nums[i]
            if sum == 0:
                max_length = i+1
            elif sum not in prefix_sum:
                prefix_sum[sum] = i
            else:
                s = prefix_sum[sum]
                e = i
                crnt_length = e - s
                max_length = max(crnt_length,max_length)
        print(prefix_sum)
        return max_length
               
               
                    

# Main function to demonstrate the examples
if __name__ == "__main__":
    solver = Solution()

    # Example 1
    nums1 = [9, -3, 3, -1, 6, -5]
    result1 = solver.longestSubarrayWithSumZero(nums1)
    print(f"Input: {nums1}")
    print(f"Result: {result1}")
    print(f"Explanation: Expected longest subarray length is 5 (e.g., [-3, 3, -1, 6, -5])")
    print("-" * 30)

    # Example 2
    nums2 = [6, -2, 2, -8, 1, 7, 4, -10]
    result2 = solver.longestSubarrayWithSumZero(nums2)
    print(f"Input: {nums2}")
    print(f"Result: {result2}")
    print(f"Explanation: Expected longest subarray length is 8 ({nums2} itself)")
    print("-" * 30)

    # Additional Test Cases (good practice for completeness)
    # nums3 = [1,-1,3,2,-2,-8,1,7,10,23]
    # result3 = solver.longestSubarrayWithSumZero(nums3)
    # print(f"Input: {nums3}")
    # print(f"Result: {result3}")
    # print(f"Explanation: Expected longest subarray length is 5 (the entire array)")
    # print("-" * 30)

    nums3 = [1, 2, 3, -3, -2, -1]
    result3 = solver.longestSubarrayWithSumZero(nums3)
    print(f"Input: {nums3}")
    print(f"Result: {result3}")
    print(f"Explanation: Expected longest subarray length is 6 (the entire array)")
    print("-" * 30)

    nums4 = [1, 2, 3] # No subarray sums to zero
    result4 = solver.longestSubarrayWithSumZero(nums4)
    print(f"Input: {nums4}")
    print(f"Result: {result4}")
    print(f"Explanation: Expected longest subarray length is 0")
    print("-" * 30)

    nums5 = [0, 0, 0] # Multiple zeros
    result5 = solver.longestSubarrayWithSumZero(nums5)
    print(f"Input: {nums5}")
    print(f"Result: {result5}")
    print(f"Explanation: Expected longest subarray length is 3")
    print("-" * 30)