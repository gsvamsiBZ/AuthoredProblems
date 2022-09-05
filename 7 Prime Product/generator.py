import random
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
def get7(n):
    l=[]
    i=7
    while i<n:
        l.append(i)
        i+=10
    return l
def getPrime7(l):
    ans=[]
    for i in l:
        if isPrime(i):
            ans.append(i)
    return ans    

n=1000000
x=get7(n)
y=getPrime7(x)
n=1000

b=random.sample(x,300)
a=random.sample(y,400)
c=[i for i in range(1,100000)]
c=random.sample(c,300)
w=a+b+c
random.shuffle(w)
print(n)
print(*w)

