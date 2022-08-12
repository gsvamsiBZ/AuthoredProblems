import random
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def getKeypad():
    s = alpha.copy()
    random.shuffle(s)
    keypad = {}
    for i in range(9):
        keypad[i+1]="".join(s[3*i:3*i+3])
    return keypad

def getQuerry(n):
    s=[]
    l=0
    while l<n:
        x=random.randint(1,9)
        if x==9:
            y=random.randint(1,2)
        else:
            y=random.randint(1,3)
        l+=y+1
        s.append(str(x)*y)
    if l>n:
        s.pop()
    return " ".join(s)


keypad = getKeypad()
for i in keypad:
    print(i,keypad[i])
n,k = 1000,100
print(n)
for i in range(n):
    q=getQuerry(k)
    print(q)