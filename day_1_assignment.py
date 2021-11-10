a="the mahabharatha is the oldest mythology"
lst=a.split()
x=0
y=0
lst2=[]
for i in a:
    y=y+1
for i in lst:
    x=x+1
for i in lst:
    if i not in lst2:
        lst2.append(i)
dic=dict()

for i in range(0,len(lst2)):
    print('number of',lst2[i],'is:',lst.count(lst2[i]))
    dic[lst2[i]]=lst.count(lst2[i])

print('\n',dic)
    
print('\nnumber of words',x)
print('\nnumber of letters',y)




###########################################

a="The mahabharatha is the oldest mythology old"
a=a.lower().split()

{i:a.count(i) for i in set(a)}

for i in set(a):
    print(i, a.count(i))
    
