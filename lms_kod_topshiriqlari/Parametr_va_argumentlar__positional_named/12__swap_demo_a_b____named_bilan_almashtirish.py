def son(a, b):
    return f"a={a} b={b}"

a, b = map(int, input().split())

print(son(a, b))
print(son(a=b, b=a))