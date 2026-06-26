x = int(input())
text = list(map(str, input().split()))
k = []
for i in text:
    if len(i) >= x:
        k.append(i)
print(k)