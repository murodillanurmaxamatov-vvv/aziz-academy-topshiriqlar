s = input().strip()
d = {}

for i in s:
    d[i] = d.get(i, 0) + 1
    
for i in sorted(d):
    print(f"{i}={d[i]}")