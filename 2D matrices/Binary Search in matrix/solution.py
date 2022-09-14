def sol(k):
    i=0
    j=c-1
    while i<r and j>=0:
        if mat[i][j]==k:
            print(i,j)
            return 
        if mat[i][j]>k:
            j-=1
        else:
            i+=1
    print(-1)


r,c=map(int,input().split())
mat=[]
for i in range(r):
    mat.append(list(map(int,input().split())))
q=int(input())
for _ in range(q):
    ele=int(input())
    sol(ele)