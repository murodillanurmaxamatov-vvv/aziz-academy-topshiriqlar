from collections import Counter
n = int(input())
s = list(map(int,input().split()))
c = Counter(s)
maks = max(c.values())
print(min(k for k, v in c.items() if v == maks))

            