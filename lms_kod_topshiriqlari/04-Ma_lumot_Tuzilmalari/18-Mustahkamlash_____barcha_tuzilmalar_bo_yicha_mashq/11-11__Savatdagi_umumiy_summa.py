n = int(input())
jami = 0

for _ in range(n):
    narx = int(input())
    son = int(input())
    m = {'narx': narx, 'son': son}
    jami += m['narx'] * m['son']
print(jami)