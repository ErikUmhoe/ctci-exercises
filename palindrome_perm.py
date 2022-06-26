class Solution:
    def has_perm_palindrome(self, s: str):
        s = s.lower().replace(' ', '')
        hashTable = {}
        # Initialize hash table containing a key for each character a-z with 0
        # Key is ordinal of character, value is number of occurrences in string
        for i in range(ord('a'), ord('z')+1):
            hashTable[i] = 0

        # Increase value in hashtable for character if it exists in the string
        for ch in s:
            hashTable[ord(ch)] += 1
        
        hasOdd = False
        for i in hashTable:
            if hashTable[i] % 2 != 0 and not hasOdd:
                hasOdd = True
            elif hashTable[i] % 2 != 0 and hasOdd:
                return False
        return True

a = Solution()
print(a.has_perm_palindrome('taco cat')) # T
print(a.has_perm_palindrome("acto tac")) # T
print(a.has_perm_palindrome('afvgh')) # F
print(a.has_perm_palindrome('taccat')) # T
print(a.has_perm_palindrome('acotac')) # F