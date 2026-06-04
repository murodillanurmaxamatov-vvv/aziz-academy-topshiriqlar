s = list(map(int,input().split()))

a = [n ** 2 if n % 2 == 0 else n for n in s]

print(*a)