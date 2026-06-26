x = int(input())

p = []

for _ in range(x):
    n, y = map(int, input().split())
    p.append((n, y))
    
b = max(p, key=lambda z: (z[0], -z[1]))

print(b[0], b[1])