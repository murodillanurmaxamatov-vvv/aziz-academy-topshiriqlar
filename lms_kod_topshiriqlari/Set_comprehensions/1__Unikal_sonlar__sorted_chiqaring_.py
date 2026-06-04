x = list(map(int, input().split()))

s = {i for i in x}

print(*sorted(s))