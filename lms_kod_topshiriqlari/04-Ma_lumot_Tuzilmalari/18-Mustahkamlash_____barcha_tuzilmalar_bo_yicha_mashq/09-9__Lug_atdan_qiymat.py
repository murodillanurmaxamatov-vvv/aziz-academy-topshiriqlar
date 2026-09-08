n = int(input())
d = {}

for _ in range(n):
    k, v = input().split()
    d[k] = v
    
t = input()
print(d[t])