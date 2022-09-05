import random

x=range(int(1e6))
l=random.sample(x,1000)
print(len(l))
print(*l)