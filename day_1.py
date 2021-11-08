us=[10,9,8,7,6,5,4,3,2,1]
for i in range(len(us)):
    for j in range(len(us)):
        if us[j]>us[i]:
            us[i],us[j]=us[j],us[i]
print(us)


us=[10,9,8,7,6,5,4,3,2,1]
sl=[]
x=1
sl[x]=us[x]
for i in range(len(us)):
    if us[x]>us[x-1]:
        sl[x],sl[x-1]=us[x-1],us[x]
print(us)



