import random
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha_lower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha_all=alpha+alpha_lower

def getword(n):
    s = alpha_all.copy()
    word = []
    for i in range(n):
        ch = random.choice(s)
        word.append(ch)
    word = "".join(word)
    return word

def getSpcl(n):
    a=alpha.copy()
    random.shuffle(a)
    x=a[:n]
    for i in range(n):
        ch=random.randint(0,1)
        if ch==1:
            x[i]=x[i].lower() 
    return x




t=100
print(t)
for _ in range(t):
    k=10
    print(*getSpcl(k),sep='')
    print(getword(1000))