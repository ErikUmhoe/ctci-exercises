from queue import LifoQueue
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = LifoQueue(len(s))
        for ch in s:
            if ch == "#" and not stack_s.empty():
                stack_s.get()
            else:
                stack_s.put(ch)
        stack_t = LifoQueue(len(t))
        for ch in t:
            if ch == "#" and not stack_t.empty():
                stack_t.get()
            else:
                stack_t.put(ch)
        res_s = ""
        while not stack_s.empty():
            ch = stack_s.get()
            if ch != "#":
                res_s += ch
        res_t = ""
        while not stack_t.empty():
            ch = stack_t.get()
            if ch != "#":
                res_t += ch
        # print(f"res_s:{res_s}, res_t: {res_t}")
        return res_s == res_t

sol = Solution()
# s = "ab#c"
# t = "ad#c"
# print(sol.backspaceCompare(s,t))
# s = "ab##"
# t = "c#d#"
# print(sol.backspaceCompare(s,t))
# s = "a#c"
# t = "b"
# print(sol.backspaceCompare(s,t))
s = "y#fo##f"
t = "y#f#o##f"
print(sol.backspaceCompare(s,t))