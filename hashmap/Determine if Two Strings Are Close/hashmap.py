word1 = "cabbba"
word2 = "abbccc"

if len(word1)!=len(word2):
    print(False)
if set(word1)!=set(word2):
    print(False)
hashm={}
hashm1={}
for i in word1:
    if i in hashm:
        hashm[i]+=1
    else:
        hashm[i]=1
for i in word2:
    if i in hashm1:
        hashm1[i]+=1
    else:
        hashm1[i]=1
if sorted(hashm.values())==sorted(hashm1.values()):
    print(True)
else:
   print(False)