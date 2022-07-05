class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        memo = [-1] * (n+1)
        index = 2
        memo[0] = 0
        memo[1] = 1
        for index in range(2, n+1):
            memo[index] = memo[index-1] + memo[index-2]
            index += 1
        print(memo)
        return memo[n]
sol = Solution()
print(sol.fib(3))