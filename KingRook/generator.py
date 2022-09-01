import random
from webbrowser import get

def getPos():
    x=random.randint(0,7)
    y=random.randint(0,7)
    return (x,y)
def kingRooks():
    l=set()
    while len(l)<3:
        l.add(getPos())
    return list(l)

n=1000
print(n)
for i in range(n):
    mat=[]
    for i in range(8):
        mat.append(['.']*8)
    k,r1,r2=kingRooks()
    mat[k[0]][k[1]]='K'
    mat[r1[0]][r1[1]]='R'
    mat[r2[0]][r2[1]]='R'
    for i in mat:
        print(*i)
    print()