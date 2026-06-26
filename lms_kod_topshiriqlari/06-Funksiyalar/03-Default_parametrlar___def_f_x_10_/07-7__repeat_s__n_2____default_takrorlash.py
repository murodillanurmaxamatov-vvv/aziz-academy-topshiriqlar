def h(a, b=2):
    return a * b

a = input()
c = input().strip()

if c == "":
    print(h(a))
else:
    print(h(a, int(c)))