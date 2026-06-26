w = input().split()
p = {(i.lower(), len(i)) for i in w}

print(len(p))
for i, l in sorted(p):
    print(f"{i}:{l}")