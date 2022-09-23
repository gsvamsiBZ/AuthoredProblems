import random
def getArray(n):
    l=[]
    while len(l)<n:
        l.append(random.randint(1,1000000000))
    return l  

t=100
print(t)
for _ in range(t):
    n=1000
    h=random.randint(n,1000000000)
    print(n,h)
    l=getArray(n)
    print(*l)