def q(d, t):
    return d * 100 // t

def b(p):
    return "%" * (p // 10) + "." * (10 - p // 10)

def make(d, t):
    p = q(d, t)
    return str(p) + "% " + b(p)

d, t = map(int, input().split())
print(make(d, t), end="")