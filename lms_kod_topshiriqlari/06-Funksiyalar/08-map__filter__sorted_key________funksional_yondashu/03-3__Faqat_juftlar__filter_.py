a = list(map(int, input().split()))
j = list(filter(lambda x: x % 2 == 0, a))
print(*j)