def s(a, b='-', c='-'):
    return f"{a} {b} {c}"

x = input().split()

if len(x) == 1:
    print(s(x[0]))
elif len(x) == 2:
    print(s(x[0], x[1]))
else:
    print(s(x[0], x[1], x[2]))