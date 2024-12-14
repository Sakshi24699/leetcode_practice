word1 = "abc"
word2 = "pqr"
l1=0
l2=0
r=[]
while l1<len(word1) and l2<len(word2):
    r.append(word1[l1])
    r.append(word2[l2])
    l1+=1
    l2+=1
if(l1<len(word1)):
    r.append(word1[l1::])
if(l2<len(word2)):
    r.append(word2[l2::])
# return r
s=''.join(r)
print(s)
