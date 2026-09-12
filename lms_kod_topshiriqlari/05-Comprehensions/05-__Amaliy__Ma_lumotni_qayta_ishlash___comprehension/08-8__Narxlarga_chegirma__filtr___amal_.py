n = list(map(int, input().split()))
a = [ i - 10 for i in n if i > 0]
print(a)