class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Better approach(TC:O(N2), SC:O(2N)+O(N))
        # my_set = set()
        # ans = []
        # for i in range(len(nums)):
        #     hashset = set()
        #     for j in range(i+1,len(nums)):
        #         ele = -1 *(nums[i]+nums[j])
        #         if ele in hashset:
        #             temp = [nums[i],nums[j],ele]
        #             temp.sort()
        #             my_set.add(tuple(temp))
        #         else:
        #              hashset.add(nums[j])
        # ans = list(my_set)
        # return ans
        # Optimal Approach - Improves space complexity to O(No of triplets) or O(1)
            ans = []
            n = len(nums)
            nums.sort()
            for i in range(n):
                if i!=0 and nums[i] == nums[i-1]:
                     continue
                j = i+1
                k = n-1
                while(j<k):
                    if nums[i]+nums[j]+nums[k] == 0:
                        ans.append([nums[i],nums[j],nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                    elif nums[i]+nums[j]+nums[k] < 0:
                        j += 1
                    else:
                        k -= 1
            return ans
                    
                           


if __name__ == "__main__":
    # Create an instance of the Solution class
    solver = Solution()

    result1 = solver.threeSum([-1, 0, 1, 2, -1, -4])
    print(f"Input: [-1, 0, 1, 2, -1, -4]\nOutput: {result1}")
    print("-" * 40)

    result2 = solver.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10])
    print(f"Input: [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]\nOutput: {result2}")
    print("-" * 40)


    # result3 = solver.threeSum([0, 0, 0])
    # print(f"Input: [0, 0, 0]\nOutput: {result3}")
    # print("-" * 40)


    # result4 = solver.threeSum([])
    # print(f"Input: []\nOutput: {result4}")
    # print("-" * 40)

    # result5 = solver.threeSum([-1, 0, 1, 2, -1, -4]) # Re-using a working example
    # print(f"Input: [-1, 0, 1, 2, -1, -4]\nOutput: {result5}")
    # print("-" * 40)