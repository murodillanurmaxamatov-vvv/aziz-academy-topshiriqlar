def d(n):
    if n == 0 or n == 1:
        return 1
    return n * d(n - 1)

def s(n):
    if n == 0:
        return 0
    return (n % 10) + s(n // 10)

n = int(input().strip())
f = d(n)
print(s(f))