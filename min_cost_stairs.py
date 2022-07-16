# 746

from typing import Dict, List

# Didnt get it. Solution notes:
# Observations of problem:
## 1: Need to get the minimum
## 2: Need to make decisions that might look different depending on previous decisions


class Solution:
# Bottom Up Dynamic Programming (Tabulation)
## Done Iteratively
## starts at base case and works its way up
## Ex: cost = [0,1,2,3,4,5]
## Start from back of list -> need to reach either 4 or 5
## Optimal to step 4 is 0 -> 2 -> 4 (cost of 2)
## Optimal to step 5 is 1 -> 3 -> 5 (cost of 4)
## Idea - finding min cost to step 4 is like solving problem w/ [0,1,2,3] (four is the top floor now)
## To solve this subproblem, need to find min cost to reach steps 2 and 3, which requires us to answer for [0,1] and [0,1,2]
## This pattern is known as RECURRENCE RELATION.
## In this case, min cost to reach ith step: minCost[i] = min(minCost[i-1], minCost[i-2] + cost[i-2])
## Base case -> start at either step 0 or 1, so minCost[0] = 0 = minCost[1]
    def bottom_minCostClimbingStairs(self, cost: List[int]) -> int:
        lenCost = len(cost)
        minimumCost = [0] * (lenCost + 1)
        for i in range(2, lenCost + 1):
            # Recurrence relation: minCost[i] = min(minCost[i-1] + cost[i-1], minCost[i-2] + cost[i-2])
            minimumCost[i] = min(minimumCost[i-1] + cost[i-1], minimumCost[i-2] + cost[i-2])
        return minimumCost[-1]

# Top Down Dynamic Programming (Recursion + Memoization)
## Starts from the top and works down to base case
## Usually implemented through recursion, and made efficient w/ memoization
## Memoization is storing results of expensive function calls in order to avoid duplicate computations
## minCost(i) is the minimum cost to reach ith step
## RECURRENCE RELATION: minCost(i) = min(minCost(i-1) + cost(i-1), minCost(i-2) + cost(i-2))
## Problem - repeated computations
## !!!! Use hashmap to store previously done computations !!!!
    def top_minCostClimbingStairs(self, cost: List[int]) -> int:
        hashMap = {}
        return self.minCost(len(cost), hashMap, cost)
        
    def minCost(self, i: int, memo: Dict, cost: List[int]) -> int:
        if i <= 1:
            return 0
        if i in memo:
            return memo[i]
        down_one = self.minCost(i-1, memo, cost) + cost[i-1]
        down_two = self.minCost(i-2, memo, cost) + cost[i-2]
        memo[i] = min(down_one, down_two)
        return memo[i]
        
                
        
    
sol = Solution()
cost = [1,100,1,1,1,100,1,1,100,1]
print(sol.top_minCostClimbingStairs(cost))
cost = [10,15,20]
print(sol.top_minCostClimbingStairs(cost))