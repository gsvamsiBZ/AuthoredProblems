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
    n=100
    print(n)
    mat=getSqMat(n)
    for i in mat:
        print(*i)

