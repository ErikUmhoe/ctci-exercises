import sys
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0.0
        curr_avg = 0.0
        max_avg = float(-sys.maxsize)
        for i in range(len(nums)):
            curr_sum += nums[i]
            if i >= k-1:
                curr_avg = curr_sum / k
                max_avg = max(max_avg, curr_avg)
                curr_sum -= nums[i-(k-1)]
        return max_avg
    
sol = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(sol.findMaxAverage(nums, k))
print(sol.findMaxAverage([5], 1))