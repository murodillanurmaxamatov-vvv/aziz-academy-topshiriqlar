def r(a, b, c):
    return f"a={a} b={b} c={c}"

x, y, z = map(int, input().split())

print(r(x, y, z))
print(r(c=x, b=y, a=z))