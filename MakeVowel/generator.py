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


n,k = 100,1000
print(n)
for i in range(n):
    print(getword(k))