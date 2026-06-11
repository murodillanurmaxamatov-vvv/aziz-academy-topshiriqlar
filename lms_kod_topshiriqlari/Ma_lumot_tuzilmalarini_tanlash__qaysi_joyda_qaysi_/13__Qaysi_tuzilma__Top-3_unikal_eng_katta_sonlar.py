n = list(map(int, input().split()))

u = set(n)

t = sorted(u, reverse=True)[:3]

print(*t)