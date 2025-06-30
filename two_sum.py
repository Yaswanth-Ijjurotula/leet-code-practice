class Solution:
    def twoSum(self, nums: list[int], target: int):
        index_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in index_map:
                index_map[nums[i]] = i
            else:
                # return [index_map[diff],i]
                return "Yes"
        # return[-1,-1]
        return "No"

    
if __name__ == "__main__":
    solver = Solution()
    nums1_v1 = [2, 6, 5, 8, 11]
    target1_v1 = 14
    print(f"Input: nums={nums1_v1}, target={target1_v1}")
    print(f"Result (Variant 1): {solver.twoSum(nums1_v1, target1_v1)}") # Expected: True

    nums2_v1 = [3, 2, 4]
    target2_v1 = 6
    print(f"Input: nums={nums2_v1}, target={target2_v1}")
    print(f"Result (Variant 1): {solver.twoSum(nums2_v1, target2_v1)}") # Expected: True

    nums3_v1 = [1, 2, 3, 4]
    target3_v1 = 10
    print(f"Input: nums={nums3_v1}, target={target3_v1}")
    print(f"Result (Variant 1): {solver.twoSum(nums3_v1, target3_v1)}") # Expected: False