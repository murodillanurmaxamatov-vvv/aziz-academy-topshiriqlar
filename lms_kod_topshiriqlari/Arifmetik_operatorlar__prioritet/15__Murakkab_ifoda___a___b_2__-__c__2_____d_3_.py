a, b, c, d = map(int,input().split())
result = (a + b*2) - (c//2) + (d%3) + (1 if c % 2 == 0 else -1)

print("Result:",result)
