n = int(input())
s = list(map(int,input().split()))
m = None
for i in s:
    if i % 2 != 0:
        if m is None or i > m:
            m = i
if m is None:
    print('No')
else:
    print(m)