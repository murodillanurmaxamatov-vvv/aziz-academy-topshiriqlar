total = 0
while True:
    number = int(input())
    if number % 2 != 0:
        break
    total += number
print(total)