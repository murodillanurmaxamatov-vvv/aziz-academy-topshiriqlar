def x(a, b=2):
    return a ** b

p = list(map(int, input().split()))

if len(p) == 1:
    print(x(p[0]))
else:
    print(x(p[0], p[1]))