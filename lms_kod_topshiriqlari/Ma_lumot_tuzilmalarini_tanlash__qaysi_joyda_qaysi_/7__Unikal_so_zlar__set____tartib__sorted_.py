w = input().split()

u = set(i.lower() for i in w)

print(*sorted(u))