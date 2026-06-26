x = list(map(int, input().split()))

count = len(x)
total = sum(x)
mn = min(x)
mx = max(x)
m = total / count

evens = 0
odds = 0

for i in x:
    if i % 2 == 0:
        evens += 1
    else:
        odds += 1
print(f"count: {count}")
print(f"sum: {total}")
print(f"min: {mn}")
print(f"max: {mx}")
print(f"mean: {m:.2f}")
print(f"evens: {evens}")
print(f"odds: {odds}")