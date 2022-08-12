keys = {}
for _ in range(9):
    key, values = input().split()
    keys[key] = values
n = int(input())
for i in range(n):
    s = input().split()
    ans = []
    for i in s:
        ans.append(keys[i[0]][len(i)-1])
    print("".join(ans))