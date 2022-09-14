for _ in range(int(input())):
    r,c=map(int,input().split())
    l=[]
    for i in range(r):
        l.append(list(map(int,input().split())))

    mat=[[0 for i in range(r)]for j in range(c)]
    sj=r
    for i in range(r):
        si=0
        sj-=1
        for j in range(c):
            mat[si][sj]=l[i][j]
            si+=1
    print(c,r)     
    for i in mat:
        print(*i)
    # print()