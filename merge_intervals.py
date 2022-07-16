import sys
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        st = sorted(intervals)
        res = []
        i = 1
        start = 0
        while i < len(st):
            if st[i-1][1] >= st[i][0]:
                i += 1
            else:
                print(f"i: {i}")
                res.append([st[start][0], st[i-1][1]])
                start = i
                i += 1
        if start == i -1:
            res.append(st[-1])
        return res

sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(intervals))
                
                