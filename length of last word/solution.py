s = "   fly me   to   the moon  "
end=len(s)-1
while s[end]==" ":
    end-=1
start=end
while start>=0 and s[start]!=" ":
    start-=1
print(end-start)