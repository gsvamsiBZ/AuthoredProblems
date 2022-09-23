import random

d=["1","2","3","4","5","6","7","8","9","0"]
f=["1","2","3","4","5","6","7","8","9"]

def getnum():
    s=[]
    s.append(random.choice(f))
    while len(s)<=100:
        s.append(random.choice(d))
    print("".join(s))
    
t=1000
print(t)
for i in  range(t):
    getnum()