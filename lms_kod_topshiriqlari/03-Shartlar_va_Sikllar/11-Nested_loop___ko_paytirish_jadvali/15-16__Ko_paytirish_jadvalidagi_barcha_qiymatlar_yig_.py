v = int(input())

y = 0
for i in range(1, v + 1):
    for j in range(1, v + 1):
        y += i * j
print(y)