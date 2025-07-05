class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        consecutive_max = 0  # Initialize to 0 since max consecutive ones cannot be negative
        for i in range(len(nums)):
            if nums[i] == 1:  # Direct comparison with 1
                count += 1
            else:
                count = 0
            consecutive_max = max(count, consecutive_max)
        return consecutive_max


def main():
    s = Solution()

    # Example 1: Standard case with a clear sequence
    nums1 = [1, 1, 0, 1, 1, 1]
    expected1 = 3
    result1 = s.findMaxConsecutiveOnes(nums1)
    print(f"Input: {nums1}, Output: {result1}, Expected: {expected1}")

    # Example 2: No ones in the array
    nums2 = [0, 0, 0, 0]
    expected2 = 0
    result2 = s.findMaxConsecutiveOnes(nums2)
    print(f"Input: {nums2}, Output: {result2}, Expected: {expected2}")

    # Example 3: All ones in the array
    nums3 = [1, 1, 1, 1, 1]
    expected3 = 5
    result3 = s.findMaxConsecutiveOnes(nums3)
    print(f"Input: {nums3}, Output: {result3}, Expected: {expected3}")

    # Example 4: A mixed array with ones at the beginning and end
    nums4 = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1]
    expected4 = 3
    result4 = s.findMaxConsecutiveOnes(nums4)
    print(f"Input: {nums4}, Output: {result4}, Expected: {expected4}")

if __name__ == "__main__":
    main()