# 438 - Array, sliding window, hash table

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        ht = Counter(p)
        result = []
        for i in range(len(s)):
            if i >= k - 1:
                ch = s[(i - k + 1):i + 1]
                curr = Counter(ch)
                if curr == ht:
                    result.append(i - k + 1)
        return result
                
sol = Solution()
s = "cbaebabacd"
p = "abc"
print(sol.findAnagrams(s, p)) # [0,6]
s = "abab"
p = "ab"
print(sol.findAnagrams(s, p)) # [0,1,2]
s = "baa"
p = "aa"
print(sol.findAnagrams(s, p)) # [1]
s = "abacbabc"
p = "abc"
print(sol.findAnagrams(s, p)) # [1,2,3,5]
s = "ababababab"
p = "aab"
print(sol.findAnagrams(s, p)) # [0,2,4,6]