# 746 - Easy
# Topics: Array, Dynamic Programming

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        totalCost = 0
        index = 2
        lenCost = len(cost)
        ht = {0: cost[0], 1: cost[1]}
        while index < lenCost:
            ht[index] = min(cost[index - 1], cost[index - 2])
            index += 1 if cost[index - 1] < cost[index - 2] else 2
        for i in range(lenCost-1):
            totalCost += min(ht[i], ht[i+1])
        return totalCost
    
    
sol = Solution()
print(sol.minCostClimbingStairs([10,15,20]))
cost = [1,100,1,1,1,100,1,1,100,1]
print(sol.minCostClimbingStairs(cost))