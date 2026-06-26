def diff(a, b):
    return a - b

a, b = map(int, input().split())

print(diff(a, b))
print(diff(b=a, a=b))