x = sorted(list(map(int, input().split())))
n = len(x)
if n % 2 == 1:
    m = x[n // 2]
else:
    m = (x[n // 2 - 1] + x[n // 2]) / 2
print(f"{m:.2f}")