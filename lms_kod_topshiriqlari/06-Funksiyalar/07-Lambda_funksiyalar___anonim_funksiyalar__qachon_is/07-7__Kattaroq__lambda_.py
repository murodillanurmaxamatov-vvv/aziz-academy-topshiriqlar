a, b = map(int, input().split())

y = lambda x, v: max(x, v)
print(y(a, b))