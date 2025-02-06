candies = [2, 3, 5, 1, 3]
extraCandies = 3

maxc = max(candies)
op = []
for i in range(len(candies)):
    tc = candies[i] + extraCandies
    if tc >= maxc:
        op.append(True)
    else:
        op.append(False)
print(op)
