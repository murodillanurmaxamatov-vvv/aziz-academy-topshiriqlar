n = list(map(int, input().split()))
s = {abs(x) for x in n}
print(*sorted(s))