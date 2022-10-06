import random
import sys
def getPoint():
    x=random.randint(-1000000,1000000)
    y=random.randint(-1000000,1000000)
    return (x,y)

def get(l):
    xmn=sys.maxsize
    ymn=sys.maxsize
    for i in l:
        xmn=min(xmn,abs(i[1]))
        ymn=min(ymn,abs(i[0]))
    return (xmn,ymn)

t=100
print(t)
for _ in range(t):
    n=1000
    print(n)
    l=set()
    temp=random.randint(900,950)
    while len(l)<temp:
        l.add(getPoint())
    x,y=get(l)
    while len(l)<n:
        l.add((random.randint(-1000000,1000000),x))
        l.add((y,random.randint(-1000000,1000000)))
    while len(l)>n:
        l.pop()
    for i in l:
        print(*i)
