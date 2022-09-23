# [Forwarded from 2010030374_Jaideep_Sharma]
for _ in range(int(input())) :
    n = int(input())
    l = input()
    # l = list(s)
    v = l.count('V')
    n = l.count('N')
    if v < n:
        print(v+v+1)
    elif n < v:
        print(n+n+1)
    else:
        print(len(l))