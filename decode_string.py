from queue import LifoQueue
class Solution:
    def decodeString(self, s: str) -> str:
        return self.decodeSubstring(s)

    def decodeSubstring(self, s: str) -> str:
        print(f"Sub string: {s}")
        length = len(s)
        i = 0
        res = ""
        digit = ""
        while i < length:
            if s[i].isdigit():
                digit += s[i]
                print(f"isdigit: i - {i}, s[i]: {s[i]}")
            elif s[i] == "[":
                j = i + 1
                numL = 1
                numR = 0
                substr = ""
                while numL != numR:
                    if s[j] == "]":
                        numR += 1
                    elif s[j] == "[":
                        numL += 1
                    else:
                        substr += s[j]
                    print(f"In second while loop, j={j}, s[j] = {s[j]}, numL={numL}, numR={numR}")
                    j += 1
                if numL != 1:
                    res = res + (int(digit) * self.decodeString(substr))
                else:
                    print(f"Digit={digit}, substr={substr}")
                    res = res + (int(digit) * substr)
                digit = ""
                i = j - 1
            else:
                res += s[i]
            i += 1
        return res
    
sol = Solution()
s = "3[a]2[bc]"
print(sol.decodeString(s))
s  = "3[a2[c]]"
print(sol.decodeString(s))