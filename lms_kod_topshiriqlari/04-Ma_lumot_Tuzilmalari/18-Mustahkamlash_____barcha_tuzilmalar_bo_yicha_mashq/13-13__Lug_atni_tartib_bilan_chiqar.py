n = int(input())
d = {}

for _ in range(n):
    k, v = input().split()
    d[k] = v
    
for i in sorted(d):
    print(i + '=' + d[i])