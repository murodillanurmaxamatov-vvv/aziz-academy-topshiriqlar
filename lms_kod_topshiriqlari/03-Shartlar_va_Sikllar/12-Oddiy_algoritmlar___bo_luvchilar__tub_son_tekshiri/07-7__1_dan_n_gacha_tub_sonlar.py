n = int(input())
for i in range(2, n + 1):
    prime = True
    for num in range(2, int(i**0.5) + 1):
        if i % num == 0:
            prime = False
            break
    if prime:
        print(i)