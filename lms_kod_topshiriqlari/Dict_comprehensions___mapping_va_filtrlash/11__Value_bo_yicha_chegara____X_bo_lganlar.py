n = int(input())

d = [input().split() for _ in range(n)]
x = int(input())

r = {key: int(value) for key, value in d if int(value) >= x}

print(r)