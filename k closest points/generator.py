import sys
def prin(a):
    sys.stdout.write(str(a)+'\n')
def input():
    return sys.stdin.readline()
t=int(input())
print(t)
for _ in range(t):
    n,k=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    n=1000
    print(n,k)
    # for i in range(n):
    #     print(*l[i])