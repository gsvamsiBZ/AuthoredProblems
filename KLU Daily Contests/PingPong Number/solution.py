def isPingPong(s):
    dif=abs(ord(s[0])-ord(s[1]))
    n=len(s)
    for i in range(1,n-1):
        if abs(ord(s[i])-ord(s[i+1])) != dif:
            return False
    return True

for _ in range(int(input())):
    n=input()
    if isPingPong(n):
        print("YES")
    else:
        print("NO")