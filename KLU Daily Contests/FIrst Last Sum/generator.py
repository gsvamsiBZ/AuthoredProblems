import random
def getNum():
    return random.randint(10000000,1000000000)

t=1000
print(t)
for i in range(t):
    print(getNum())