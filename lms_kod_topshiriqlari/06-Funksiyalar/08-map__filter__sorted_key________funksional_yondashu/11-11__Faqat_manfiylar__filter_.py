a = list(map(int, input().split()))
m = list(filter(lambda x: x < 0, a))
print(*m)