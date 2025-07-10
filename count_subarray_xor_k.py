from collections import defaultdict
class Solution:
    def count_subarr(self,nums,k):
        prefix_xor = defaultdict(int)
        prefix_xor[0]+=1
        count = 0
        xr = 0
        for i in range(len(nums)):
            xr = xr ^ nums[i]
            count += prefix_xor[xr ^ k]
            prefix_xor[xr] += 1
        return count
            
        
def main():
    s = Solution()
    # ex-1
    arr1 = [4, 2, 2, 6, 4] 
    k1 = 6 
    result1 = s.count_subarr(arr1,k1)
    print(result1)
    # ex - 2
    arr2 = [5, 6, 7, 8, 9]
    k2 = 5
    result2 = s.count_subarr(arr2,k2)
    print(result2)

if __name__ == "__main__":
    main()
