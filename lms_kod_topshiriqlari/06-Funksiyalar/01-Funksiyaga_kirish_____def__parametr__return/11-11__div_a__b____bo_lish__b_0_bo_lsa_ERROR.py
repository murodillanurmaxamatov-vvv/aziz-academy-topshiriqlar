def div(a, b):
    if b == 0:
        return "ERROR"
    return a / b

a, b = map(int, input().split())

r = div(a, b)
if r == "ERROR":
    print('ERROR')
else:
    print(f"{r:.2f}")