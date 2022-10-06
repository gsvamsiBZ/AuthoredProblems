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

t=10000
print(t)
l=[]
for _ in range(t//2):
    l.append(getword(20))
while len(l)<t:
    l.append(random.choice(l))
random.shuffle(l)
print(*l,sep="\n")
    