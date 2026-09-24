def i(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    
    return i(n // 2) + str(n % 2)

n = int(input().strip())
print(i(n))