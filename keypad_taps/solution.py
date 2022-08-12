keys={}
for _ in range(9):
    s=input()
    for i in range(len(s)):
        keys[s[i]]=i+1
n=int(input())
for i in range(n):
    word=input() 
    ans=0
    for i in word:
        ans+=keys[i]
    print(ans)   