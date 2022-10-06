import sys
t = int(input())
for _ in range(t):
    n = int(input())
    dx = sys.maxsize
    dy = sys.maxsize
    xn = 0
    yn = 0
    for i in range(n):
        x, y = map(int, input().split())
        current_dx = abs(y)
        current_dy = abs(x)
        if current_dx == dx:
            xn += 1
        elif current_dx < dx:
            xn = 1
            dx = current_dx
        if current_dy == dy:
            yn += 1
        elif current_dy < dy:
            yn = 1
            dy = current_dy
    print(dx, xn, dy, yn)
