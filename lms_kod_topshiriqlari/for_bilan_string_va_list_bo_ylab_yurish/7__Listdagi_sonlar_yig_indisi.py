n = int(input())
numbers = list(map(int,input().split()))
summa = 0
for i in range(n):
    summa += numbers[i]
print(summa)