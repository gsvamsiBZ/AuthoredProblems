import random
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def getword(n):
    s = alpha.copy()
    word = []
    for i in range(n):
        ch = random.choice(s)
        word.append(ch)
    word = "".join(word)
    return word

def getVow():
    s= alpha.copy()
    x=set()
    while len(x)<5:
        x = set(random.choices(s,k=5))
    return x

t= 100
print(t)
for _ in range(t):
    v=getVow()
    print(*v,sep='')
    n=random.randint(500,1000)
    w=getword(n)
    print(w)
