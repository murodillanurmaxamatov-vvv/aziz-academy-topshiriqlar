def p(x, y):
    return f"({x},{y})"

x, y = map(int,input().split())

print(p(x, y))
print(p(y=y, x=x))