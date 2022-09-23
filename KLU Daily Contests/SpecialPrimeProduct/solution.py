def isSpecialPrime(n):
    if n <= 3:
        return False
    i = 2
    while(i*i <= n):
        if n % i == 0:
            if i*i != n:
                return False
            return True
        i += 1
    return False

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    p = 1
    for i in l:
        if isSpecialPrime(i):
            p *= i
            p = p % 1000000007
    print(p)
