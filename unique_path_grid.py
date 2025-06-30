class Solution:
    #Recursive approach
    # def count_paths(self,i,j,m,n):
    #         count =0
    #         if i == m-1 and j == n-1:
    #             return 1
    #         if i >= m or j >= n:
    #             return 0
    #         else:
    #             count += self.count_paths(i+1,j,m,n)
    #             count += self.count_paths(i,j+1,m,n)
    #         return count
    # def uniquePaths(self, m: int, n: int) -> int:
    #     i,j=0,0
    #     return self.count_paths(i,j,m,n)
    
    #Using DP - Optimal Approach - 1
    # def count_paths(self,i,j,m,n,dp):
    #         if i == m-1 and j == n-1:
    #             return 1
    #         if i >= m or j >= n:
    #             return 0
    #         if dp[i][j] != -1:
    #              return dp[i][j]
    #         else:
    #             dp[i][j] = self.count_paths(i+1,j,m,n,dp) + self.count_paths(i,j+1,m,n,dp)
    #             return dp[i][j]
    # def uniquePaths(self, m: int, n: int) -> int:
    #     i,j=0,0
    #     dp = [[-1 for _ in range(n)]for _ in range(m)]
    #     return self.count_paths(i,j,m,n,dp)
    
    # Optimal Approach - 2 -> Using Combinations
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 1
        nn = m+n-2
        r = m-1
        for i in range(1,r+1):
            ans = ans * (nn-r+i)/i
        return int(ans)


if __name__ == "__main__":
    obj = Solution()
    totalCount = obj.uniquePaths(3, 7)
    print("The total number of Unique Paths are ", totalCount)