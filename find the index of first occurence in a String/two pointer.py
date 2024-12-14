haystack = "sadbutsad"
needle = "sad"
if len(haystack) < len(needle):
    print(-1)
s1 = 0
while s1 < len(haystack):
    s2 = 0
    index = s1

    while s1 < len(haystack) and s2 < len(needle) and haystack[s1] == needle[s2]:
        s1 += 1
        s2 += 1
        if s2 == len(needle):
            print(s1 - s2)
    s1 = index + 1
print(-1)