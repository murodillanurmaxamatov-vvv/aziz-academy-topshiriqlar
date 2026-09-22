def y(n):
    if n <= 0:
        return ''
    return "*" + y(n - 1)

n = int(input())
print(y(n))