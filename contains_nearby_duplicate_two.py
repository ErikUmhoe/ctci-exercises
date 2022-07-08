from typing import List
import queue


class Solution:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     lenNums = len(nums)
    #     for i in range(lenNums):
    #         for j in range(i+1, lenNums):
    #             if nums[i] == nums[j] and abs(i - j) <= k:
    #                 return True
    #     return False
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, j in enumerate(nums):
            if j in dic and i - dic[j] <= k:
                return True
            dic[j] = i
        return False
                
        
        
nums = [1,2,3,1]
k = 3
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))
nums = [1,2,3,1,2,3]
k = 2
print(sol.containsNearbyDuplicate(nums, k))
nums = [1,0,1,1]
k = 1
print(sol.containsNearbyDuplicate(nums, k))