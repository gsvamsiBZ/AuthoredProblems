for _ in range(int(input())):
    mat=[]
    for i in range(8):
        mat.append(input().split())
    input()
    for i in range(8):
        for j in range(8):
            if mat[i][j]=="K":
                king=(i,j)
            elif mat[i][j]=="Q":
                queen=(i,j)
    if king[0]==queen[0] or king[1]==queen[1] or king[0]+king[1]==queen[0]+queen[1] or king[0]-king[1]==queen[0]-queen[1]:
        print("Yes")
    else:
        print("No")