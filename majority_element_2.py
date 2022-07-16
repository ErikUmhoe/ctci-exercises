# 229

from collections import Counter
from typing import List


class Solution:
    # Easily solution - another Counter hash map
    # go through all keys in order of highest occurrence, recording elements, until find one w/ count < n//3
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Idea - Boyer Voting algorithm, but dynamically shrink value of n (and n//3)
        counter = Counter(nums)
        l = []
        mc = counter.most_common(2)
        l.append(mc[0][0])
        if mc[1][1] > (len(nums) // 3):
            l.append(mc[1][0])
        return l
    
sol = Solution()
nums = [3,2,3]
print(sol.majorityElement(nums))