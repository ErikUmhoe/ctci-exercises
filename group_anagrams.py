from collections import deque
from typing import List 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        for word in strs:
            hash_val = self.getHash(word)
            if hash_val not in ht:
                ht[hash_val] = deque([word])
            else:
                ht[hash_val].append(word)
        res = []
        for key in ht.keys():
            res.append(list(ht[key]))
        return res
    def getHash(self, str) -> str:
        hash_sum = 0
        for ch in str:
            hash_sum += (ord(ch) / ord(ch.upper()))
        return format(hash_sum, '.10f')
    
strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
print(sol.groupAnagrams(strs))
strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
print(sol.groupAnagrams(strs))

