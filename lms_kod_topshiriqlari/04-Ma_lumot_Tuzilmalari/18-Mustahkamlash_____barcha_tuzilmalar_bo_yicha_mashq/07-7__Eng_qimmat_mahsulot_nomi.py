n = int(input())
p = []
for _ in range(n):
    a = input()
    b = input()
    p.append({"nom": a, 'narx': b})
m = max(p, key=lambda d: d['narx'])
print(m['nom'])