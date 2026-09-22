def sss(n):
    if n == 0:
        return 0
    return (n % 10) + sss(n // 10)

n = int(input())
print(sss(n))