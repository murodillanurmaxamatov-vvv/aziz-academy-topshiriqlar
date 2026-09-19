a = list(map(int, input().split()))
k = list(filter(lambda x: x > 5, a))
print(*k)