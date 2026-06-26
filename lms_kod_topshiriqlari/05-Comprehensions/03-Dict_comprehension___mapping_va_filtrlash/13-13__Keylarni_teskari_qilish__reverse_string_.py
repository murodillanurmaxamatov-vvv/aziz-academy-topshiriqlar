n = int(input())

d = [input().split() for _ in range(n)]
r = {key[::-1]: int(value) for key, value in d}

print(r)