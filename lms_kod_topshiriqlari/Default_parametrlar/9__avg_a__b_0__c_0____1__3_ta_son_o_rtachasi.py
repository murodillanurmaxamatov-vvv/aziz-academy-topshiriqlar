def son(a, b=0, c=0):
    return (a + b + c) / 3

x = list(map(int, input().split()))

if len(x) == 1:
    r = x[0] / 1
elif len(x) == 2:
    r = (x[0] + x[1]) / 2
else:
    r = (x[0] + x[1] + x[2]) / 3
print(f"{r:.2f}")