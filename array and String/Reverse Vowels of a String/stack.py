s = "IceCreAm"

sta = []
for i in s:
    if i.lower() in "aeiou":
        sta.append(i)

rev = ""
for i in s:
    if i.lower() in "aeiou":
        rev += sta.pop(-1)
    else:
        rev += i
print(rev)
