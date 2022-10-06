import sys
def prin(a):
    sys.stdout.write(str(a)+'\n')
def input():
    return sys.stdin.readline()

dist = lambda x:x[0]**2 +x[1]**2
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    y=sorted(l,key=lambda x:x[0]**2 +x[1]**2)
    if (dist(y[k-1])==dist(y[k])):
        print("hello")