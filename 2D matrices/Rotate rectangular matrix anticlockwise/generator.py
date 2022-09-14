import random

def getSqMat(n):
    mat=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j]=random.randint(-1000,1000)
    return mat

def getMat(r,c):
    mat=[[0 for i in range(c)]for j in range(r)]
    for i in range(r):
        for j in range(c):
            mat[i][j]=random.randint(-1000,1000)
    return mat

t= 100
print(t)
for _ in range(t):
    r=random.randint(80,100)
    c=random.randint(40,100)
    print(r,c)
    mat=getMat(r,c)
    for i in mat:
        print(*i)

