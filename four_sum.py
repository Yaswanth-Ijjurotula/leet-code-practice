class Solution:
    def four_c_sum(self,nums,t):
        # Better Approach(O(N3))
        # n = len(nums)
        # my_set = set()
        # ans = []
        # for i in range(n):
        #     for j in range(i+1,n):
        #         hashset = set()
        #         for k in range(j+1,n):
        #             ele = t-(nums[i]+nums[j]+nums[k])
        #             if ele in hashset:
        #                 temp = [nums[i],nums[j],nums[k],ele]
        #                 temp.sort()
        #                 my_set.add(tuple(temp))
        #             else:
        #                 hashset.add(nums[k])
        # ans = list(my_set)
        # return ans

        #Optimal Approach
        n = len(nums)
        ans = []
        if n < 4:
            return ans
        nums.sort()
        
        for i in range(n):
            if(i!=0 and nums[i]==nums[i-1]):
                continue
            for j in range(i+1,n):
                if(j!=i+1 and nums[j]==nums[j-1]):
                    continue
                k = j+1
                l = n-1
                while(k<l):
                    c_sum = nums[i]+ nums[j]+nums[k]+nums[l]
                    if c_sum == t:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        ans.append(temp)
                        k+=1
                        l-=1
                        while(k<l and nums[k] == nums[k-1]):
                              k+=1
                        while(k<l and nums[l] == nums[l+1]):
                             l-=1
                    elif(c_sum < t):
                        k += 1
                    else:
                        l-=1

        return ans

            
         

def main():
    s = Solution()

    # Example 1: Standard case with multiple solutions and negatives
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    # Expected output: A list of lists, e.g., [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    # Note: The order of quadruplets and elements within them might vary
    # depending on the specific algorithm, but the sets of numbers should match.
    result1 = s.four_c_sum(nums1,target1)
    print(f"Input nums: {nums1}, Target: {target1}, Output: {result1}")
    # For actual testing, you'd compare sorted versions of results.

    # Example 2: Array with duplicates, leading to one specific solution
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    # Expected output: [[2,2,2,2]]
    result2 = s.four_c_sum(nums2, target2)
    print(f"Input nums: {nums2}, Target: {target2}, Output: {result2}")

    # Example 3: No solution found
    nums3 = [1, 2, 3, 4, 5]
    target3 = 100
    # Expected output: []
    result3 = s.four_c_sum(nums3, target3)
    print(f"Input nums: {nums3}, Target: {target3}, Output: {result3}")

    # Example 4: Mixed numbers including negatives, with multiple solutions
    nums4 = [-1, 0, 1, 2, -1, -4]
    target4 = -1
    # Expected output: [[-4,0,1,2],[-1,-1,0,1]]
    result4 = s.four_c_sum(nums4, target4)
    print(f"Input nums: {nums4}, Target: {target4}, Output: {result4}")


if __name__ == "__main__":
    main()