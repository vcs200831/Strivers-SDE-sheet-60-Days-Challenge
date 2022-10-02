class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for j in range(target+2)] for i in range(n+1)]
    
        dp[0][0] = 1

        for rem_d in range(1, n+1):
            for tot_S in range(0, target + 2):
                for a in range(1,min(k+1,tot_S + 1)):
                     dp[rem_d][tot_S] += dp[rem_d-1][tot_S - a]
        return dp[n][target]%(10**9+7)