def x(a, b):
    return min(a, b)

def s(a, b):
    return max(a, b)

def d(a, b):
    return f"{(a + b) / 2:.2f}"

a, b = map(int, input().split())

print(x(a, b))
print(s(a, b))
print(d(a, b))