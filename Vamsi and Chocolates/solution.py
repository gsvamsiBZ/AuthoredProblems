import sys
def prin(a):
    sys.stdout.write(str(a)+'\n')
def input():
    return sys.stdin.readline()
import math
def sol(n):
    ans=0
    for i in l:
        ans+=math.ceil(i/n)
    return ans<=h
for _ in range(int(input())):
    n,h=map(int,input().split())
    l=list(map(int,input().split()))
    low=1
    high=int(1e9)
    while low<=high:
        mid=(low+high)//2
        if sol(mid):
            high=mid-1
        else:
            low=mid+1
    print(low)