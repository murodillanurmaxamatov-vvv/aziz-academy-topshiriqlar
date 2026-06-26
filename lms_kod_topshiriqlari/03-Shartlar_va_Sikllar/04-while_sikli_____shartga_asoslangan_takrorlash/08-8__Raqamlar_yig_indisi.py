n = int(input())
yigindi = 0

while n > 0:
    raqam = n % 10
    yigindi += raqam
    n //= 10
print(yigindi)