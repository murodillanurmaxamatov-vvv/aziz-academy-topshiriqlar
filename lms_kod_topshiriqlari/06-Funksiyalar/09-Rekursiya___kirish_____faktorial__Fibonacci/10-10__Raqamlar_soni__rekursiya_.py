def s(n):
    if n < 10:
        return 1
    return 1 + s(n // 10)

n = int(input())
print(s(abs(n)))