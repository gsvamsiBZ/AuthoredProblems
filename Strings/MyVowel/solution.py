import sys
for _ in range(int(input())):
    v=set(input())
    w=input()
    c=0
    for i in w:
        if i in v:
            c+=1
    print(c)