lst=[1,1,2,3,4,5,5,6,7,8,9,9,10]
dst=dict()

for i in lst:
    if i not in dst.keys():
        dst[i]=1
    else:
        dst[i]+=1

print(dst)


lst=[1,1,2,3,4,5,5,6,7,8,9,9,10]

st=[0]*11

for i in lst:
    st[i]+=1
    
print(st)





        
        
