class str_compress:
    def compress_str(self, s: str):
        count = 1
        curr_char = s[0]
        new_str = ""
        array = []
        for i in range(1, len(s)):
            if curr_char == s[i]:
                count += 1
            else:
                array.append((curr_char, count))
                # new_str += f"{curr_char}{count}"
                curr_char = s[i]
                count = 1
        if s[-2] == s[-1]:
            #new_str += f"{curr_char}{count}"
            array.append((curr_char, count))
        else:
            # new_str += f"{s[-1]}1"
            array.append((s[-1], 1))
        new_str = ''.join([f"{a}{b}" for (a,b) in array])
        if len(new_str) >= len(s):
            return s
        
        return new_str

a = str_compress()
print(a.compress_str('aaaabbbccca'))
print(a.compress_str('abcdefg'))
print(a.compress_str('aabbccddeeffgg'))
print(a.compress_str('aaabbccddeeffgg'))
