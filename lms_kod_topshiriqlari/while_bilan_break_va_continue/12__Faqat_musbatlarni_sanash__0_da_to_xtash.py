count = 0
while True:
    number = int(input())
    if number == 0:
        break
    if number < 0:
        continue
    count += 1
print(count)