def nom(a, b, c):
    return (a + b + c, a * b * c, max(a, b, c), min(a, b, c))

a, b, c = map(int, input().split())

x = nom(a, b, c)
x1 = nom(c=c, a=a, b=b)


print("pos:",*x)
print("named:",*x1)