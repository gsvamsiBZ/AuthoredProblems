import random
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def getKeypad():
    s = alpha.copy()
    random.shuffle(s)
    keypad = {}
    for i in range(9):
        keypad[i+1]="".join(s[3*i:3*i+3])
    return keypad

def getword(n):
    s = alpha.copy()
    word = []
    for i in range(n):
        ch = random.choice(s)
        word.append(ch)
    word = "".join(word)
    return word

keypad = getKeypad()
for i in keypad:
    print(i,keypad[i])
n,k = 1000,100
print(n)
for i in range(n):
    print(getword(k))