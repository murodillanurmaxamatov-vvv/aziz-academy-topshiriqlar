def y(name='Guest'):
    return f"Hello, {name}!"
s = input().strip()

if s:
    print(y(s))
else:
    print(y())
    