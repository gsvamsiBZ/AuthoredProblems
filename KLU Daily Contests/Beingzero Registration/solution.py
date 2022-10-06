d={}
for _ in range(int(input())):
    s=input()
    if s not in d:
        print("SUCCESSFULLY REGISTERED")
        d[s]=1
    else:
        print(s,d[s],sep='')
        d[s]+=1    