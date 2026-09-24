def p(n):
    if n < 10:
        return n
    return (n % 10) * p(n // 10)

n = int(input().strip())
print(p(n))