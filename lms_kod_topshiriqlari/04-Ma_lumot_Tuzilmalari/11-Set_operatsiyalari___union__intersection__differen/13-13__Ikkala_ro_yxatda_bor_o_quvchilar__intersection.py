A = set(input().strip().split())
B = set(input().strip().split())

c = sorted(A & B)

print(len(c))
for name in c:
    print(name)
