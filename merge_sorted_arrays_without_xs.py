def swapifgreater(arr1,arr2,ind1,ind2):
        if(arr1[ind1]>arr2[ind2]):
            arr1[ind1],arr2[ind2] = arr2[ind2],arr1[ind1]
    
def merge(arr1, arr2, n, m):
    #BF approach
    # arr3 = [0]*(n+m)
    # i,j,index = 0,0,0
    # while(i<n and j<m):
    #     if(arr1[i]<=arr2[j]):
    #         arr3[index] = arr1[i]
    #         index += 1
    #         i += 1
    #     else:
    #         arr3[index] = arr2[j]
    #         index +=1
    #         j += 1
    # while(i<n):
    #     arr3[index] = arr1[i]
    #     index += 1
    #     i += 1
    # while(j<m):
    #     arr3[index] = arr2[j]
    #     index += 1
    #     j += 1
    # for i in range(n+m):
    #     if i < n:
    #         arr1[i] = arr3[i]
    #     else:
    #         arr2[i-n] = arr3[i]
    # return arr1,arr2
    
    # Optimal Approach-1
    # i,j = n-1,0
    # while(i >= 0 and j < m):
    #     if arr1[i] > arr2[j]:
    #         arr1[i],arr2[j] = arr2[j],arr1[i]
    #         i -= 1
    #         j += 1
    #     else:
    #         break
    # arr1.sort()
    # arr2.sort()
    # return arr1,arr2

    #Optimal Approach - 2(GAP method or shell sort)
    len = n+m
    gap = (len+1)//2
    while(gap > 0):
        left = 0
        right = left + gap
        while(right < len):
            #arr1 and arr2
            if left<n and right >=n:
                swapifgreater(arr1,arr2,left,right-n)
            #arr2 and arr2
            elif left >= n:
                 swapifgreater(arr2,arr2,left-n,right-n)
            #arr1 and arr1
            else:
                 swapifgreater(arr1,arr1,left,right)
            left+=1
            right+=1
        if gap ==1:
             break
        gap = (gap+1)//2
    return arr1,arr2
                 

if __name__ == '__main__':
    arr1 = [1, 4, 8, 10]
    arr2 = [2, 3, 9]
    n = 4
    m = 3
    merge(arr1, arr2, n, m)

    print("The merged arrays are:")
    print("arr1[] = ", end="")
    for i in range(n):
        print(arr1[i], end=" ")
    print("\narr2[] = ", end="")
    for i in range(m):
        print(arr2[i], end=" ")
    print() 

