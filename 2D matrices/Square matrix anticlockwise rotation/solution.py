def trans(l,r,c):
    for i in range(r):
        for j in range(i+1,c):
            l[i][j],l[j][i]=l[j][i],l[i][j]
def revrow(l,r,c):
    for i in range(r):
        a=0
        b=c-1
        while(a<b):
            l[i][a],l[i][b]=l[i][b],l[i][a]
            a+=1
            b-=1
def revcol(l,r,c):
    for i in range(c):
        a=0
        b=r-1
        while a<b:
            l[a][i],l[b][i]=l[b][i],l[a][i]
            a+=1
            b-=1

for _ in range(int(input())):
    n=int(input())
    mat=[]
    for i in range(n):
        mat.append(list(map(int,input().split())))
    trans(mat,n,n)
    revcol(mat,n,n)
    for i in mat:
        print(*i)
    print()
