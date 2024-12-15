arr = [1,2,2,1,1,3]
hm={}
for i in arr:
    if i in hm.keys():
        hm[i]+=1
    else:
        hm[i]=1
l=list(hm.values())
if(len(l))==len(set(l)):
    print(True)
else:
    print(False)