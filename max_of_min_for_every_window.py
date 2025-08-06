class Solution:
    def maxOfMinOfWindows(self, arr: list[int]) -> list[int]:
        n = len(arr)
        if n == 0:
            return []
        left = [-1] * n
        stack = [] 
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1]
            stack.append(i)

        right = [n] * n
        stack = [] 

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if not stack:
                right[i] = n
            else:
                right[i] = stack[-1]
            stack.append(i)
        
        ans = [0] * n

        for i in range(n):
            length = right[i] - left[i] - 1
            ans[length - 1] = max(ans[length - 1], arr[i])

        for k in range(n - 2, -1, -1):
            ans[k] = max(ans[k], ans[k+1])

        return ans

# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1 from problem description
    arr1 = [10, 20, 30, 50, 10, 70, 30]
    expected1 = [70, 30, 20, 10, 10, 10, 10]
    result1 = sol.maxOfMinOfWindows(arr1)
    print(f"Input: {arr1}")
    print(f"Output: {result1}")
    print(f"Expected: {expected1}")
    print(f"Match: {result1 == expected1}\n")

    # Test Case 2: All increasing
    arr2 = [1, 2, 3, 4, 5]
    expected2 = [5, 4, 3, 2, 1]
    result2 = sol.maxOfMinOfWindows(arr2)
    print(f"Input: {arr2}")
    print(f"Output: {result2}")
    print(f"Expected: {expected2}")
    print(f"Match: {result2 == expected2}\n")

    # Test Case 3: All decreasing
    arr3 = [5, 4, 3, 2, 1]
    expected3 = [5, 4, 3, 2, 1]
    result3 = sol.maxOfMinOfWindows(arr3)
    print(f"Input: {arr3}")
    print(f"Output: {result3}")
    print(f"Expected: {expected3}")
    print(f"Match: {result3 == expected3}\n")
    
    # Test Case 4: Array with duplicates and varying order
    arr4 = [10, 5, 20, 10, 5, 15]
    expected4 = [20, 10, 5, 5, 5, 5]
    result4 = sol.maxOfMinOfWindows(arr4)
    print(f"Input: {arr4}")
    print(f"Output: {result4}")
    print(f"Expected: {expected4}")
    print(f"Match: {result4 == expected4}\n")

    # Test Case 5: Single element
    arr5 = [42]
    expected5 = [42]
    result5 = sol.maxOfMinOfWindows(arr5)
    print(f"Input: {arr5}")
    print(f"Output: {result5}")
    print(f"Expected: {expected5}")
    print(f"Match: {result5 == expected5}\n")