def kop(a, b, c):
    return a + b * c

a, b, c = map(int, input().split())

print(kop(a, b, c))
print(kop(a, c=c, b=b))