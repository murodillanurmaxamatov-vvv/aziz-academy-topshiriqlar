def p(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return  False
    return True

a, b = map(int, input().split())

c = 0
for nn in range(a, b + 1):
    if p(nn):
        c += 1
print(c)