n = int(input())

d = [input().split() for _ in range(n)]

result = {key: int(value) * 2 for key, value in d}
print(result)