n = int(input())

d = [input().split() for _ in range(n)]

r = {
    key: "even" if int(value) % 2 == 0 else "odd"
    for key, value in d
}

print(r)