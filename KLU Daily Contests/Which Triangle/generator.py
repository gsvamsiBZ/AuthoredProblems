import random
def getSides():
    x=random.randint(1000,10000000)
    y=random.randint(1000,10000000)
    z=random.randint(1000,10000000)
    ch=random.randint(1,100)
    if ch>=80:
        # print('jsgfjkvjkbjkbcvx')
        return (x,x,x)
    if ch>=70:
        return (x,x,y)
    if ch>60:
        return (x,y,x)
    if ch>50:
        return (y,x,x)
    return (x,y,z)

t=1000
print(t)
for i in range(t):
    print(*getSides())
