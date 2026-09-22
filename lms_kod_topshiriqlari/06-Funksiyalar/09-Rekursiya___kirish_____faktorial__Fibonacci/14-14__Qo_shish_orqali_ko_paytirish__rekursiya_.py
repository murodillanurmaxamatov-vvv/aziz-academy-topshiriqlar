def s(a, b):
    if b == 0:
        return 0
    return a + s(a, b - 1)

a, b = map(int, input().split())
print(s(a, b))