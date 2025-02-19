word1 = "abc"
word2 = "pqr"
r=""
for i in range(min(len(word1), len(word2) )):
    r+=word1[i]
    r+=word2[i]
if len(word1)>len(word2):
    r+=word1[i+1:]
if len(word2)>len(word1):
    r+=word2[i+1:]
print(r)