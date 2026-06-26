n = int(input())

d = {}

for _ in range(n):
    x, m = input().split()
    d[x] = m
    
q = int(input())

for _ in range(q):
    z = input().strip()
    print(d.get(z, "NOT_FOUND"))