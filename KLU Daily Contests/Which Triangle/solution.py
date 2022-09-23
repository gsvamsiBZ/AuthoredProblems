for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a+b>c and b+c>a and c+a>b:
        if a==b and b==c:
            print("Equilateral Triangle")
        elif a==b or b==c or c==a:
            print("Isosceles Triangle") 
        else:
            print("Scalene Triangle")
    else:
        print("Not a Triangle")