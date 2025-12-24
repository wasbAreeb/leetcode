
strs = ["flower","flow","flight"]

c_string = ""
for i in range(2):
    for j in range(len(strs[i])):
        if len(strs[i]) < len(strs[i+1]):
            if strs[i][j] == strs[i+1][j]:
                c_string += str(strs[i][j])

count = 0
for i in range(len(strs)):
    if c_string in strs[i]:
        count += 1
   
if count == len(strs):
    print(c_string)
else:
    print("")

    