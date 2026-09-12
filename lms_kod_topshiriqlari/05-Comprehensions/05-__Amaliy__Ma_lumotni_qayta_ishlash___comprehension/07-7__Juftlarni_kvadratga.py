x = list(map(int, input().split()))
na = [i ** 2 for i in x if i % 2 == 0]
print(na)