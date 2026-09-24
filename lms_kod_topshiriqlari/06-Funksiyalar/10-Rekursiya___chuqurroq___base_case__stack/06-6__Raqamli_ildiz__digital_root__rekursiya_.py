def p(n):
    if n == 0:
        return 0
    return (n % 10) + p (n // 10)

def d(n):
    if n < 10:
        return n
    return d(p(n))

n = int(input().strip())
print(d(n))