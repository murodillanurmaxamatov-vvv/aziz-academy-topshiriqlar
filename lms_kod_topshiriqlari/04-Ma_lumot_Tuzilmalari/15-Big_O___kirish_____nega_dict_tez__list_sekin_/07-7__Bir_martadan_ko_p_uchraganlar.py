from collections import Counter
s = list(map(int, input().split()))
a = Counter(s)
print(sum(1 for i in a.values() if i > 1))