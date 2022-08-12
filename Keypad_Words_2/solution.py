keys = {}
for _ in range(9):
    key, values = input().split()
    vlen = len(values)
    for i in range(vlen):
        keys[values[i]]=key*(i+1) 
n = int(input())
for i in range(n):
    word = input()
    for i in word:
        print(keys[i],end=' ')
    print()