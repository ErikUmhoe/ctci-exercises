from queue import LifoQueue

def isValid(s):
    stk = LifoQueue()
    ht = {
        "{": "}",
        "(":")",
        "[":"]"
    }
    for c in s:
        if c in ht:
            stk.put(c)
        else:
            if stk.empty():
                return False
            open = stk.get()
            if ht[open] != c:
                return False
    return stk.empty()
    
a = ["(","[","(","{","}",")","]",")"]
print(isValid(a))