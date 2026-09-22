def d(n):
    if n == 0:
        return 1
    return 3 * d(n - 1)

n = int(input())
print(d(n))