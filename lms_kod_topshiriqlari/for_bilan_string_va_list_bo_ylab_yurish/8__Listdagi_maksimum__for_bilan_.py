n = int(input())
numbers = list(map(int,input().split()))
katta = numbers[0]
for i in range(1, n):
    if numbers[i] > katta:
        katta = numbers[i]
print(katta)