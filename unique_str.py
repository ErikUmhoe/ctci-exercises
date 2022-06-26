class Solution:
    def string_unique(self, s: str):
        charTable = {}
        for ch in s:
            if ord(ch) in charTable.keys():
                return False
            else:
                hash = ord(ch)
                charTable[hash] = ch
        return True
a = Solution()
print(a.string_unique("abcd"))
print(a.string_unique("bcbc"))