class Solution:
    def removeDuplicates(self, nums):
        # BF Approach 
        # st = set()
        # for i in range(len(nums)):
        #     st.add(nums[i])
        # k = len(st)
        # j = 0
        # for x in st:
        #     nums[j] = x
        #     j += 1
        # return k

        #Optimal Approach
        n = len(nums)
        i = 0
        for j in range(i+1,n):
             if nums[i]!=nums[j]:
                  nums[i+1] = nums[j]
                  i += 1
        return i+1
        
    

def main():
    s = Solution()
    # 1. Empty Array
    nums1 = []
    k1 = s.removeDuplicates(nums1)
    print(f"Input: {[]}, Output (k): {k1}, Array: {nums1[:k1]}, Expected k: 0, Expected Array: []")

    # 2. Single Element Array
    nums2 = [1]
    k2 = s.removeDuplicates(nums2)
    print(f"Input: {[1]}, Output (k): {k2}, Array: {nums2[:k2]}, Expected k: 1, Expected Array: [1]")

    # 3. Array with No Duplicates
    nums3 = [1, 2, 3, 4, 5]
    k3 = s.removeDuplicates(nums3)
    print(f"Input: {[1, 2, 3, 4, 5]}, Output (k): {k3}, Array: {nums3[:k3]}, Expected k: 5, Expected Array: [1, 2, 3, 4, 5]")

    # 4. Array with All Duplicates
    nums4 = [7, 7, 7, 7, 7]
    k4 = s.removeDuplicates(nums4)
    print(f"Input: {[7, 7, 7, 7, 7]}, Output (k): {k4}, Array: {nums4[:k4]}, Expected k: 1, Expected Array: [7]")

    # 5. Standard Case with Duplicates
    nums5 = [1, 1, 2, 2, 3]
    k5 = s.removeDuplicates(nums5)
    print(f"Input: {[1, 1, 2, 2, 3]}, Output (k): {k5}, Array: {nums5[:k5]}, Expected k: 3, Expected Array: [1, 2, 3]")

    # 6. More Complex Standard Case
    nums6 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k6 = s.removeDuplicates(nums6)
    print(f"Input: {[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]}, Output (k): {k6}, Array: {nums6[:k6]}, Expected k: 5, Expected Array: [0, 1, 2, 3, 4] ")

    # 7. Duplicates at the Beginning
    nums7 = [1, 1, 1, 2, 3, 4]
    k7 = s.removeDuplicates(nums7)
    print(f"Input: {[1, 1, 1, 2, 3, 4]}, Output (k): {k7}, Array: {nums7[:k7]}, Expected k: 4, Expected Array: [1, 2, 3, 4]")

    # 8. Duplicates at the End
    nums8 = [1, 2, 3, 4, 4, 4]
    k8 = s.removeDuplicates(nums8)
    print(f"Input: {[1, 2, 3, 4, 4, 4]}, Output (k): {k8}, Array: {nums8[:k8]}, Expected k: 4, Expected Array: [1, 2, 3, 4]")

    # 9. Duplicates in the Middle
    nums9 = [1, 2, 2, 3, 4]
    k9 = s.removeDuplicates(nums9)
    print(f"Input: {[1, 2, 2, 3, 4]}, Output (k): {k9}, Array: {nums9[:k9]}, Expected k: 4, Expected Array: [1, 2, 3, 4]")

    # 10. Array with Negative Numbers
    nums10 = [-3, -3, -1, 0, 0, 0, 1, 1, 2]
    k10 = s.removeDuplicates(nums10)
    print(f"Input: {[-3, -3, -1, 0, 0, 0, 1, 1, 2]}, Output (k): {k10}, Array: {nums10[:k10]}, Expected k: 5, Expected Array: [-3, -1, 0, 1, 2]")

    # 11. Large Array (for performance check)
    nums11 = [i // 2 for i in range(10000)]
    # Create a copy for printing original input if needed, as nums11 will be modified
    nums11_original_len = len(nums11)
    k11 = s.removeDuplicates(nums11)
    print(f"Input: large array of len {nums11_original_len}, Output (k): {k11}, Expected k: 5000")
    # Note: Printing the full large array can be very long, so we just print its effective length.

if __name__ == "__main__":
        main()