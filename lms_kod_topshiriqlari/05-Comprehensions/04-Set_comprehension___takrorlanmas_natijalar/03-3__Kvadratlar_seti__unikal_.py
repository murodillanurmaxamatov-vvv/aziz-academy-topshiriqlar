n = list(map(int,input().split()))

s = {x * x for x in n}
print(*sorted(s))