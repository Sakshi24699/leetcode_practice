gain = [-5, 1, 5, 0, -7]
maxa = 0
curr = 0
for i in range(len(gain)):
    curr += gain[i]
    maxa = max(maxa, curr)
print(maxa)
