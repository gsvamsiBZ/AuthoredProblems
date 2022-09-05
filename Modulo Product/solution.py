import sys
n= int(input())
l=list(map(int,input().split()))
p=1
mod=int(1e9+7)
for i in l:
    p=p*i
    p=p%(mod)

print(p)