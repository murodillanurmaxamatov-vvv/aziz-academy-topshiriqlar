def t(p, r=12):
    return p * (1 + r / 100)

x = list(map(int, input().split()))

if len(x) == 1:
    r = t(x[0])
else:
    r = t(x[0], x[1])
print(f"{r:.2f}")