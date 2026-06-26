def son(a, b):
    return a - a * b / 100

a, b = map(int, input().split())

print(f"{son(a, b):.2f}")
print(f"{son(b=b, a=a):.2f}")