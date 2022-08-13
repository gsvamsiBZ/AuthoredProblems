from collections import Counter
import sys


def countRemovals(s, t):
    s = Counter(s)
    t = Counter(t)
    ans = sys.maxsize
    for i in t:
        if i not in s:
            return 0
        ans = min(ans, s[i]//t[i])
    return ans


for _ in range(int(input())):
    s, t = input().split()
    print(countRemovals(s, t))
