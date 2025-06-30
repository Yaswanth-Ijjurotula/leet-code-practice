def find_majority_element(nums):
    #BF Approach -O(N2)
    # l = len(nums)
    # tar = l//2
    # for i in range(l-1):
    #     count = 1 
    #     for j in range(i+1,l):
    #         if(nums[i] == nums[j]):
    #             count += 1
    #             print(count)
    #         if(count > tar):
    #             return nums[i]
    #     return -1
   
    #Better Approach - Linear time with extra space.
    l = len(nums)
    tar = l//2
    hmap = {}
    for i in range(l):
        if nums[i] not in hmap:
            hmap[nums[i]] = 1
        else:
            hmap[nums[i]] += 1
    for i in hmap:
        if hmap[i] > tar:
            return i

    # Optimal Approach - Moore's voting Algorithm
    # l = len(nums)
    # tar = l//2
    # ele = None
    # count = 0
    # counter = 0
    # for i in range(l):
    #     if count == 0:
    #         ele = nums[i]
    #         count = 1
    #     elif(nums[i]== ele):
    #         count +=1
    #     else:
    #         count -=1
        
    # for j in range(l):
    #     if(nums[j]==ele):
    #         counter +=1
    #     if counter > tar:
    #         return ele


if __name__ == "__main__":
    # Example 1:
    nums1 = [3, 2, 3]
    result1 = find_majority_element(nums1)
    print(f"Input: {nums1}, Result: {result1}") # Expected: 3

    # Example 2:
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    result2 = find_majority_element(nums2)
    print(f"Input: {nums2}, Result: {result2}") # Expected: 2

    # Example 3:
    nums3 = [4, 4, 2, 4, 3, 4, 4, 3, 2, 4]
    result3 = find_majority_element(nums3)
    print(f"Input: {nums3}, Result: {result3}") # Expected: 4
