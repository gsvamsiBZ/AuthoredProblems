import sys
def isPrime(n):
    if n==2:
        return True
    if n==1 or n&1==0:
        return False
    i=3
    while(i*i<=n):
        if n%i==0:
            return False
        i+=2
    return True
n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
    if i%10 ==7 and isPrime(i):
        # print(i)
        sum+=i
        sum=sum%1000003
print(sum)
