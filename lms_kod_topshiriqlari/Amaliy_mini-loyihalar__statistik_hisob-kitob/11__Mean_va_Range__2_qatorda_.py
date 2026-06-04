x = list(map(int,input().split()))
m = sum(x) / len(x)
r = max(x) - min(x)

print(f"{m:.2f}")
print(r)