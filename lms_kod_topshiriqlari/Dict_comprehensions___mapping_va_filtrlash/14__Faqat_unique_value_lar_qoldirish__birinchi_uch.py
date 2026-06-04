n = int(input())

d = [input().split() for _ in range(n)]

seen = set()

r = {
    key: int(value)
    for key, value in d
    if value not in seen and not seen.add(value)
}
print(r)