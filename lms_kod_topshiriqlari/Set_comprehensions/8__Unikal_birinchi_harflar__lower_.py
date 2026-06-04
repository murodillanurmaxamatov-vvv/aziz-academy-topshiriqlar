w = input().split()

s = {i[0].lower() for i in w}
print(*sorted(s))