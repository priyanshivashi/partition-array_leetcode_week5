class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    
        n = len(arr)
        
        def tabulation():
            dp = [0]*(n + 1)
            for i in range(n - 1, -1,-1):
                maxi = -1e9
                res = -1e9
                for m in range(i, min(n, i + k)):
                    maxi = max(maxi, arr[m])
                    ans = maxi * (m - i + 1) + dp[m + 1]
                    res = max(ans, res)

                dp[i] = res
            return dp[0]
        
        return tabulation()
