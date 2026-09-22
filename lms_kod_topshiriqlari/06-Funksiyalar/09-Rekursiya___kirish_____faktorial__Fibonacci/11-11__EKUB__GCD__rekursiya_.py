def e(a, b):
    if b == 0:
        return a
    return e(b, a % b)

a, b = map(int, input().split())
print(e(a, b))