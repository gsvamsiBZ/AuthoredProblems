t=int(input())
for _ in range(t):
    mat=[]
    for i in range(8):
        mat.append(input().split())
    if _!=(t-1):
        input()
    rooks=[]
    for i in range(8):
        for j in range(8):
            if mat[i][j]=="K":
                king=(i,j)
            elif mat[i][j]=="R":
                rooks.append((i,j))
    for rook in rooks:
        if king[0]==rook[0] or king[1]==rook[1]:
            print("Yes")
            break
    else:
        print("No")