n = int(input())
maxx = 0
for i in range(1, n):
    if n % i == 0:
        maxx = i
print(maxx)