a="the mahabharatha is the oldest mythology"
lst=a.split()
x=0
lst2=[]

for i in lst:
    x=x+1
for i in lst:
    if i not in lst2:
        lst2.append(i)
for i in range(0,len(lst2)):
    print('number of',lst2[i],'is:',lst.count(lst2[i]))
    
print('\nnumber of words',x)