n = int(input())
d = {}
for _ in range(n):
    i, b = input().split()
    d[i] = int(b)
    
print(sum(d.values()))