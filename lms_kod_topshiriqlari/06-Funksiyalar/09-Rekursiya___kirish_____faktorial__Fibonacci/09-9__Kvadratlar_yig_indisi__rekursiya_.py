def qosh(n):
    if n <= 1:
        return n
    return n ** 2 + qosh(n - 1)

n = int(input())
print(qosh(n))