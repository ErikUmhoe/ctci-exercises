class Solution:
    def longestPalindrome(self, s: str) -> int:
        lenS = len(s)
        chars = set(s)
        ht = {}
        for ch in chars:
            ht[ch] = False
        longest = 0
        if lenS == 1:
            return 1
        index = lenS - 1
        while index >= 0:
            if ht[s[index]]:
                longest += 2
            ht[s[index]] = not ht[s[index]]
            index -= 1
        for ch in chars:
            if ht[ch]:
                longest += 1
                break
        return longest