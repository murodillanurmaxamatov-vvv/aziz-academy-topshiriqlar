n = int(input())

data = [input().split() for _ in range(n)]

result = {key: int(value) ** 2 for key, value in data}

print(result)