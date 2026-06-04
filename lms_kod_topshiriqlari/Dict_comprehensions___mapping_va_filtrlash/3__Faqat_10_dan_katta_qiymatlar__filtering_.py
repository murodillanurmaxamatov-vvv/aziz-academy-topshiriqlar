n = int(input())

d = [input().split() for _ in range(n)]

r = {key: int(value) for key, value in d if int(value) > 10}
print(r)