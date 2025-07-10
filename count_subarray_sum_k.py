from collections import defaultdict

class Solution:
    def count_subarray(self,nums,k):
        n = len(nums)
        prefix_sum = defaultdict(int)
        crnt_sum = 0
        count = 0
        prefix_sum[0] += 1
        for i in range(n):
            crnt_sum += nums[i]
            count += prefix_sum[crnt_sum - k]
            prefix_sum[crnt_sum]+=1
        return count
            
        

def main():
    s = Solution()
    # ex-1
    arr1 = [3, 1, 2, 4]
    k1 = 6 
    result1 = s.count_subarray(arr1,k1)
    print(result1)
    # ex - 2
    arr2 = [1,2,3]
    k2 = 3
    result2 = s.count_subarray(arr2,k2)
    print(result2)

if __name__ == "__main__":
    main()
