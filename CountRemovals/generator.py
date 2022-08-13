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


n=100
slen,tlen = 1000,100
print(n)
for i in range(n):
    t = getword(tlen)
    x = random.randint(0,9)
    s=list(t*x)
    random.shuffle(s)
    s="".join(s)
    x=slen-len(s)
    s+=getword(x)
    print(s,t) 