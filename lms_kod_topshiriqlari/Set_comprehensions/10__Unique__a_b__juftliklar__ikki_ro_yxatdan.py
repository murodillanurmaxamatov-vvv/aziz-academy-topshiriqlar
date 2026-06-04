A = list(map(int, input().split()))
B = list(map(int, input().split()))

p = {(a, b) for a in A for b in B}

print(len(p))

for a, b in sorted(p):
    print(f"{a},{b}")