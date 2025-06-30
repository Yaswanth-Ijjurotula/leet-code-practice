def searchMatrix(matrix, target):
    #my approach
    # if not matrix:
    #     return False
    # target_row = -1

    # for i in range(len(matrix)-1):
    #     if matrix[i][0] <= target and matrix[i+1][0]> target:
    #         target_row = i
    
    # for j in range(len(matrix[target_row])):
    #     if matrix[target_row][j] == target:
    #         return True
    # return False
    
    # Optimal Approach - flattened 2D into 1D Array:
    if not matrix:
         return False
    n = len(matrix)
    m = len(matrix[0])
    low = 0
    high = n * m - 1
    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

if __name__ == "__main__":
    # Example 1: Target found
    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target1 = 16
    print(f"Searching for {target1} in matrix1: {searchMatrix(matrix1, target1)}")  # Expected: True

    # Example 2: Target not found
    matrix2 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target2 = 13
    print(f"Searching for {target2} in matrix2: {searchMatrix(matrix2, target2)}")  # Expected: False

    # Example 3: Empty matrix
    matrix3 = []
    target3 = 5
    print(f"Searching for {target3} in empty matrix: {searchMatrix(matrix3, target3)}")  # Expected: False

    # Example 4: Matrix with one row
    matrix4 = [[1, 2, 3, 4]]
    target4_1 = 3
    target4_2 = 5
    print(f"Searching for {target4_1} in single-row matrix: {searchMatrix(matrix4, target4_1)}") # Expected: True
    print(f"Searching for {target4_2} in single-row matrix: {searchMatrix(matrix4, target4_2)}") # Expected: False

    # Example 5: Matrix with one column
    matrix5 = [
        [1],
        [5],
        [9]
    ]
    target5_1 = 9
    target5_2 = 7
    print(f"Searching for {target5_1} in single-column matrix: {searchMatrix(matrix5, target5_1)}") # Expected: True
    print(f"Searching for {target5_2} in single-column matrix: {searchMatrix(matrix5, target5_2)}") # Expected: False

    # Example 6: Target at beginning/end
    matrix6 = [
        [1, 2],
        [3, 4]
    ]
    target6_1 = 1
    target6_2 = 4
    print(f"Searching for {target6_1} (first element): {searchMatrix(matrix6, target6_1)}") # Expected: True
    print(f"Searching for {target6_2} (last element): {searchMatrix(matrix6, target6_2)}")  # Expected: True