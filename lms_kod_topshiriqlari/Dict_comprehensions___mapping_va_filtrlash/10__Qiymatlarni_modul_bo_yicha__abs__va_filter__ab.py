n = int(input())

d = [input().split() for _ in range(n)]

r = {
    key: abs(int(value))
    for key, value in d
    if abs(int(value)) >= 5
}
print(r)