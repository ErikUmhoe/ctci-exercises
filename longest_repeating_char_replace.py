# 424 - Medium
# Hashtable, string, sliding window

from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        res = 0
        l = 0
        for i in range(len(s)):
            ch = s[i]
            counter[ch] += 1
            while (i - l + 1) - counter.most_common(1)[0][1] > k:
                counter[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res

sol = Solution()
s = "ABAB"
k = 2
print(sol.characterReplacement(s, k))           
s = "AABABBA"
k = 1
print(sol.characterReplacement(s, k))
s = "BAAA"
k = 0
print(sol.characterReplacement(s, k))
s = "ABBB"
k = 2
print(sol.characterReplacement(s, k))               