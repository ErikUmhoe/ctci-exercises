from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        return self.binarySearch(nums, low, high, target)
    def binarySearch(self, nums: List[int], low: int, high: int, target: int):
        if high >= low:
            mid = (high+low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binarySearch(nums, low, mid-1, target)
            else:
                return self.binarySearch(nums, mid+1, high, target)
        else:
            return -1
sol = Solution()
q1 = ([1,4,6,7,9,12,54], 6) #2
q2 = ([1,2,3,4,5,6,7,8,9], 10) #-1
print(sol.search(q1[0], q1[1]))
print(sol.search(q2[0], q2[1]))