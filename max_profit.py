class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lenP = len(prices)
        return self._maxProfit(prices, lenP - 1, sys.maxsize, 0, 0)
        
    def _maxProfit(self, prices, index, low, high, profit) -> int:
        if index < 0:
            return profit
        else:
            if high - prices[index] > profit:
                profit = high - prices[index]
                low = prices[index]
            elif prices[index] > high:
                high = prices[index]
        return self._maxProfit(prices, index - 1, low, high, profit)