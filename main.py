

strs = ["flower","flow","flight"]

c_string = ""
for i in range(2):
    for j in range(len(strs[i])):
            print(strs[i+1][j])
            # if strs[i][j] == strs[i+1][j]:
            #     c_string += str(strs[i][j])

print(c_string)