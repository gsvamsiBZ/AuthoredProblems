import random
def getDimensions():
    r=random.randint(3,100)
    c=random.randint(3,100)
    return (r,c)
t=10
print(t)
for _ in range(t):
    print(*getDimensions())