w = input().split()

s = {x.lower() for x in w}

print(*sorted(s))