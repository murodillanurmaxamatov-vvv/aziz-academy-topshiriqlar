def son(a, b):
    return f"sum: {a + b}\ndiff: {a - b}\nprod: {a * b}"

a, b = map(int, input().split())

print(son(a, b))