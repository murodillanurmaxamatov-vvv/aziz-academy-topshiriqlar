n = int(input())

d = [input().split() for _ in range(n)]

r = {key: int(value) for key, value in d if int(value) % 2 == 0}
print(r)