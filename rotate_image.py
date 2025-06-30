from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #BF Approach-1
        # m = len(matrix)
        # n = len(matrix[0])
        # result_m = [[0 for _ in range(m)] for _ in range(n)]
        # for i in range(m):
        #     k = 0
        #     for j in range(n-1,-1,-1):
        #         result_m[i][j] = matrix[k][i]
        #         k += 1
        # print(result_m)
        # return result_m

        # Optimal approach
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n-1):
            for j in range(i+1,n):
                if(i != j):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    sol = Solution()
    print(sol.rotate(matrix))