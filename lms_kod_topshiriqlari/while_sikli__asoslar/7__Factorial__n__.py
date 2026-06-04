n = int(input())
factorial = 1
count = 1
while count <= n:
    factorial *= count
    count += 1
print(factorial)