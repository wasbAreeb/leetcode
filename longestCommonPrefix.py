
# 24/12/2025

def main(str):
    strs = sorted(strs, key=len)

    c_string = ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if char != s[i]:
                return c_string
                exit()
        c_string += char

    return c_string

