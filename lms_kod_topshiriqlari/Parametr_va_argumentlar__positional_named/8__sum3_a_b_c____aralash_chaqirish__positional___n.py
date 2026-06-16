def qosh(a, b, c):
    return a + b + c

a, b, c = map(int,input().split())

print(qosh(a, b, c))
print(qosh(a, b=b, c=c))