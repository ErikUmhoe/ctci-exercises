# Shamelessly ripped from https://youtu.be/3SJ3pUkPQMc
# Find all intervals where an increase occurs, e.g. if prices[i] is 1 for i = 1 and price[j] = 5 for j = 2, that is an increase
# Buy at i and sell at j
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i - 1]
        return profit