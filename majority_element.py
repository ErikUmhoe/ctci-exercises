# 169

from collections import Counter
from typing import List


class Solution:
    # Hash map
    # O(n) time, O(n) space
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        print(counter)
        return counter.most_common(1)[0][0]
    
    
    # Boyer-Moore Voting Algorithm
    # O(n) time, O(1) space
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
    
sol = Solution()
nums = [3,2,3]
print(sol.majorityElement(nums))
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))