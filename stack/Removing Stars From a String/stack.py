s = "leet**cod*e"
sta = []
for i in s:
    if i == '*':
        sta.pop()

    else:
        sta.append(i)
print(''.join(sta))
