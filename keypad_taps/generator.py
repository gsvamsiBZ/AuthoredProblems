import random
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def getKeypad():
    s = alpha.copy()
    # random.shuffle(s)
    keypad = []
    for i in range(9):
        keypad.append("".join(s[3*i:3*i+3]))
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
print(*keypad,sep="\n")
n,k = 5,3
print(n)
for i in range(n):
    print(getword(k))