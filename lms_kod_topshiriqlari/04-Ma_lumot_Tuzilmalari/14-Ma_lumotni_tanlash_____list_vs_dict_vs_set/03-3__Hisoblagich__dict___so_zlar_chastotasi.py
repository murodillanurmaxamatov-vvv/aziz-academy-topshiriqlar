x = input().split()

f = {}

for i in x:
    i = i.lower()
    f[i] = f.get(i, 0) + 1
    
for z in sorted(f):
    print(z, f[z])