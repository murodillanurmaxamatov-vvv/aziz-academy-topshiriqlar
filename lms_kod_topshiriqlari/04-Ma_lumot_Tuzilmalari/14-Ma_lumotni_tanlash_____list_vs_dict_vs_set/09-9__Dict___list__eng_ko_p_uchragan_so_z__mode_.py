w = input().split()

f = {}

for i in w:
    i = i.lower()
    f[i] = f.get(i, 0) + 1
    
b = None
c = -1

for z, y in f.items():
    if y > c:
        b = z
        c = y
    elif y == c and z < b:
        b = z
        
print(b, c)

