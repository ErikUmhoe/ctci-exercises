class One_Away:
    
    def remove_at_index(self, s: str, i: int):
        new_str = s[:i] + s[i+1:]
        #print(f"Removed char {s[i]} at index {i} from {s}.")
        return new_str

    def try_replace_char(self, a: str, b: str, i: int):
        for x in range(ord('a'), ord('z') + 1):
            new_str = a[:i] + chr(x) + a[i+1:]
            if new_str == b:
                return True
        return False

    def is_one_away(self, a: str, b: str):
        if a == b:
            return True
        if abs(len(a) - len(b)) > 1:
            return False
        idx = 0
        diffCount = 0
        if len(a) == len(b):
            for i in range(0, len(a)):
                if a[i] != a[i]:
                    idx = i
                    diffCount += 1
            if diffCount > 1:
                return False
            else:
                return self.try_replace_char(a, b, idx)
        
        longer = a if len(a) > len(b) else b
        shorter = a if len(a) < len(b) else b
        for i in range(0, len(longer)):
            new_str = self.remove_at_index(longer, i)
            if new_str == shorter:
                return True
        return False
        
sol = One_Away()
print(sol.is_one_away('pales', 'pale'))
print(sol.is_one_away('bale', 'pale'))
print(sol.is_one_away('pale', 'bake'))
print(sol.is_one_away('palessssssssssssssssssssssssssss', 'bake'))