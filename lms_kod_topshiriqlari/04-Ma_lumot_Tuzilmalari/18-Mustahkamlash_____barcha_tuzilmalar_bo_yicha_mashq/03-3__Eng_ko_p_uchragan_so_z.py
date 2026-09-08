w = input().split()
counts = {}

for i in w:
    counts[i] = counts.get(i, 0) + 1
print(max(counts, key=counts.get))