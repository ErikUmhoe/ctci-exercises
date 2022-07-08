from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for n in range(len(stones)):
            stones[n] = stones[n] * -1
        print(stones)
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            print(f"s1: {s1}")
            print(f"s2: {s2}")
            if s1 != s2:
                diff = s1 - s2
                heapq.heappush(stones, diff)
        if len(stones) < 1:
            return 0
        return stones[0] * -1
    
sol = Solution()
stones = [2,7,4,1,8,1]
print(sol.lastStoneWeight(stones))
stones = [1]
print(sol.lastStoneWeight(stones))