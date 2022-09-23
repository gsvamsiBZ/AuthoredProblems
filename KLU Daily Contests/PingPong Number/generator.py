import random
def getPingPong(n):
    dig=['1','2','3','4','5','6','7','8','9','0']
    f=['1','2','3','4','5','6','7','8','9']
    s=[]
    diff= random.randint(0,5)
    s.append(random.choice(f))
    while len(s)<n:
        last=int(s[-1])
        a=last+diff
        b=last-diff
        x=[]
        if a>=0 and a<10 :
            x.append(a)
        if b>=0 and b<10:
            x.append(b)
        s.append(str(random.choice(x)))
    return "".join(s)

def change(s):
    dig=['1','2','3','4','5','6','7','8','9','0']
    l=list(s)
    x=random.randint(-5,-1)
    l[x]=random.choice(dig)
    return "".join(l)
    
t=1000
print(t)
for i in range(t):
    p=getPingPong(18)
    ch=random.randint(1,20)
    if ch>=16:
        p=change(p)
    print(p)