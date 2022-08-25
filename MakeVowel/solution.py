import sys
vowels = ['A', 'E', 'I', 'O', 'U', '[']
for _ in range(int(input())):
    s = input()
    min_ops = 0
    for ch in s:
        ops = sys.maxsize
        for v in vowels:
            ops = min(ops, abs(ord(ch)-ord(v)))
        min_ops += ops
    print(min_ops)