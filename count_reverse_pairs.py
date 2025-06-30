def count_r_pairs(low,mid,high,nums):
    cnt = 0
    r = mid+1
    for i in range(low,mid+1):
        while(r <= high and nums[i] > 2* nums[r]):
            r += 1
        cnt = cnt + (r-(mid+1))
    return cnt
        
def merge(low,mid,high,nums):
    temp = []
    left = low
    right = mid+1
    while(left <= mid and right<=high):
        if(nums[left]<=nums[right]):
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1
    while(left <= mid):
        temp.append(nums[left])
        left+=1
    while(right <= high):
        temp.append(nums[right])
        right+=1
    for i in range(low,high+1):
        nums[i] = temp[i-low]

def merge_sort(nums,low,high):
    cnt = 0
    if(low >= high):
        return cnt
    mid = (low+high)//2
    cnt += merge_sort(nums,low,mid)
    cnt += merge_sort(nums,mid+1,high)
    cnt += count_r_pairs(low,mid,high,nums)
    merge(low,mid,high,nums)
    return cnt

if __name__ == "__main__":
    nums = [40,25,19,12,9,6,2]
    n = 7
    print(merge_sort(nums,0,n-1))
    