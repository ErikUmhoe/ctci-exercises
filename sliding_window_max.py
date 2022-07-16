from collections import deque
import sys
from typing import List
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        queue = deque()
        heap = []
        lenNums = len(nums)
        curr_max = -sys.maxsize
        result = []
        for i in range(lenNums):
            queue.append(nums[i])
            if i >= (k - 1):
                if nums[i] >= curr_max:
                    curr_max = nums[i]
                popped = queue.popleft()
                heapq.heappush(heap, nums[i] * -1)
                result.append(curr_max)
                if popped == curr_max:
                    heapq.heappop(heap)
                heapq.heappush(heap, nums[i] * -1)
                curr_max = heapq.nsmallest(1, heap)[0] * -1
            else:
                heapq.heappush(heap, nums[i] * -1)
                if nums[i] > curr_max:
                    curr_max = nums[i]
        return result
    
    
sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sol.maxSlidingWindow(nums, k))
nums = [1, -1]
k = 1
print(sol.maxSlidingWindow(nums, k))