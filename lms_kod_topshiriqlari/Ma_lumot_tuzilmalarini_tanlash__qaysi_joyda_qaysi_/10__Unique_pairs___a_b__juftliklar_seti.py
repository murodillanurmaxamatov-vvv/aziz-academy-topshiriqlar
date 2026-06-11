A = list(map(int, input().split()))
B = list(map(int, input().split()))

p = set()

for a in A:
    for b in B:
        p.add((a, b))
        
p = sorted(p)

print(len(p))
for a, b in p:
    print(a, b)