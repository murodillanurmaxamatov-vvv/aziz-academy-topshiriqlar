x = list(map(int,input().split()))

m = sum(x) / len(x)
r = max(x) - min(x)

if r == 0:
    c = [0.0 for _ in x]
else:
    c = [(i - m) / r for i in x]
print(" ".join(f"{z:.2f}" for z in c))