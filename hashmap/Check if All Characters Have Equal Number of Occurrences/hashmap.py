s = "abacbc"
hm = {}
for i in s:
    if i in hm:
        hm[i] += 1
    else:
        hm[i] = 1
print(len(set(hm.values())) == 1)
# r=hm[s[0]]
# for i in hm:
#     if hm[i]!=r:
#         return False
# return True
