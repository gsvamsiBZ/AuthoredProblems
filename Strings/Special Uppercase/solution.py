x=[0,1,3]
while len(x)<=250:
    x.append(x[-1]+2*x[-2])
try:
    while(True):
        n=int(input())
        print(x[n])
except:
    pass