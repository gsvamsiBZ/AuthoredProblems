for _ in range(int(input())):
    r,c=map(int,input().split())
    for i in range(r):
        for j in range(c):
            if i==0 or j==0 or i==r-1 or j==c-1:
                print("0",end="")
            else:
                print(" ",end="")
        print()
    print()