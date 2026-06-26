def a(x, c='UZS'):
    return f"{x} {c}"

t = input().split()

if len(t) == 1:
    print(a(int(t[0])))
else:
    print(a(int(t[0]), t[1]))