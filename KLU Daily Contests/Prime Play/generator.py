import random
def getnum():
    ch= random.randint(1,4)
    if ch==4:
        return random.randint(1,1000000000)
    x=random.randint(1,10)
    y=random.randint(1,10)
    z=random.randint(1,10)
    num= (2**x)*(3**y)*(5**z)
    return num


t=100
print(t)
for i in range(t):
    print(getnum())