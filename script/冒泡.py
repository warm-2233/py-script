

a=[3,0,8,2]
print(a)

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        print('---',a)
        if len(a)-i==j:print('--__--')
        if a[j] > a[j+1]:
            t=a[j+1]
            a[j+1]=a[j]
            a[j]=t


print(a)
"----------------------------"


a=[3,0,258,2,5,12, 6]
length = len(a) - 1
print(a, length)

for i in range(length):
    print('**',a, '**')
    for j in range(length-i):
        print(a, end=' ')
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]
        print('---',a)
            
print(a)






