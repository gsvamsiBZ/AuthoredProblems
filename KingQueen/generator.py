import random
def kingQueen():
    x=random.randint(0,7)
    y=random.randint(0,7)
    a=random.randint(0,7)
    b=random.randint(0,7)
    if x==a and y==b:
        return kingQueen()
    return ([(x,y),(a,b)])

n=100
print(n)
for i in range(n):
    mat=[]
    for i in range(8):
        mat.append(['.']*8)
    k,q=kingQueen()
    mat[k[0]][k[1]]='K'
    mat[q[0]][q[1]]='Q'
    for i in mat:
        print(*i)
    print()