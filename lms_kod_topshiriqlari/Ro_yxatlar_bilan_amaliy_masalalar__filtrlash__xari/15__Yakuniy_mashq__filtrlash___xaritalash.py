n = int(input())
x = list(map(int, input().split()))

r = [x * 2 for x in x if x > 0]

print(r)