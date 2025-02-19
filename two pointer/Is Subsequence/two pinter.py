s = "abc"
t = "ahbgdc"

l = 0
r = 0
while r < len(t) and l < len(s):
    if s[l] == t[r]:
        l += 1
    r += 1
print(l == len(s))
