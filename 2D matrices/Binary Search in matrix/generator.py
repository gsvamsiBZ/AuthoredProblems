import random
def getArray(n):
    l=set()
    while len(l)<n:
        l.add(random.randint(1,10000000))
    l=list(l)
    l.sort()
    return l  
print(100,100)
mat=getArray(10000)
c=0
for i in range(100):
    for j in range(100):
        print(mat[c],end=" ")
        c+=1
    print()
q=100000
print(q)
for i in range(q):
    ch=random.randint(1,30)
    if ch%10==0:
        print(10000002)
    else:
        if ch>28:
            w=random.randint(-200,-100)
        else:
            w=random.randint(-20,-1)
        print(mat[ch])