def ca(a, b, c):
    if a < b:
        return b
    if a > c:
        return c
    return a

def i(a, b, c):
    return b <= a <= c

def n(a, b, c):
    return (a - b) / (c- b)

a, b, c = map(int, input().split())
print(ca(a, b, c))
print(i(a, b, c))
print(f"{n(a, b, c):.2f}")