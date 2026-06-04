numbers = []
while True:
    num = float(input())
    if num == 0:
        break
    numbers.append(num)
    
if len(numbers) == 0:
    print(0)
else:
    average = sum(numbers) / len(numbers)
    print(average)