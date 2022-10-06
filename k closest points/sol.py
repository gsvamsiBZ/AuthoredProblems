import sys
def prin(a):
    sys.stdout.write(str(a)+'\n')
def input():
    return sys.stdin.readline()

for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    y=sorted(l,key=lambda x:x[0]**2 +x[1]**2)
    temp=y[:k]
    temp.sort()
    for i in temp:
        print(*i)