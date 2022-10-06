import sys
def sol(arr,n,l,d):
    if arr[0]>d:
        return False
    for i in range(1,n):
        if arr[i]-arr[i-1]>d:
            return False
    if l-arr[-1]>d:
        return False
    return True


t = int(input())
for _ in range(t):
    n,l,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort()
    