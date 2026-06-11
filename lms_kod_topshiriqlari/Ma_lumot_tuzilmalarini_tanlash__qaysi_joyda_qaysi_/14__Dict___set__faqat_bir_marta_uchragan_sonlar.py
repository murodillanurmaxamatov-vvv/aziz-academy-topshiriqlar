n = list(map(int, input().split()))
f = {}

for i in n:
    f[i] = f.get(i, 0) + 1
    
r = [i for i, x in f.items() if x == 1]

if not r:
    print("EMPTY")
else:
    print(*sorted(r))