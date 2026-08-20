n = int(input())
d = {}

for _ in range(n):
    a = input().strip()
    d[a] = d.get(a, 0) + 1
    
i = input().strip()
print(d.get(i, 0))