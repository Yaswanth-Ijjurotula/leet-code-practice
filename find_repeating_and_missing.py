from typing import List, Tuple

class Solution:
    def find_repeated_and_missing(self, nums: List[int]) -> List[int]:
        #Approach -1
        # ans=[]
        # freq = [0] * (len(nums)+1)
        # for i in range(len(nums)):
        #     freq[nums[i]] += 1
        # for j in range(1,len(nums)+1):
        #     if freq[j] == 0:
        #         ans.append(j)
        #     if freq[j] > 1:
        #         ans.append(j)
        # return ans

        #Optimal approach - Math
        n = len(nums)
        Sn = (n*(n+1))/2
        S2n = (n*(n+1)*((2*n)+1))/6
        S,S2 = 0,0
        for i in range(n):
            S = S + nums[i]
            S2 = S2 + (nums[i] * nums[i])
        val1 = S - Sn
        val2 = S2 - S2n
        val2 = val2/val1
        x = (val1 + val2)/2
        y = val2 - x
        return[x,y]
# Example Call:
if __name__ == "__main__":
    solver = Solution()

    # Example from your prompt
    nums1 = [3, 1, 2, 5, 3]
    repeated1, missing1 = solver.find_repeated_and_missing(nums1)
    print(f"Input: {nums1}, Repeated: {repeated1}, Missing: {missing1}")
    # Expected Output: Input: [3, 1, 2, 5, 3], Repeated: 3, Missing: 4

    # Another example
    nums2 = [1, 2, 2, 4]
    repeated2, missing2 = solver.find_repeated_and_missing(nums2)
    print(f"Input: {nums2}, Repeated: {repeated2}, Missing: {missing2}")
    # Expected Output: Input: [1, 2, 2, 4], Repeated: 2, Missing: 3