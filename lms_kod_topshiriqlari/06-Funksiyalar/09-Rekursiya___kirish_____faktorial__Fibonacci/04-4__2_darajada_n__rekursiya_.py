def qwe(n):
    if n == 0:
        return 1
    return 2 * qwe(n - 1)

n = int(input())
print(qwe(n))