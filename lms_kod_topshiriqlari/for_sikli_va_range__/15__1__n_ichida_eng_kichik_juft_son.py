n = int(input())
kichik = None
for i in range(1, n + 1):
    if i % 2 == 0:
        if kichik is None or i < kichik:
            kichik = i
if kichik is not None:
    print(kichik)
else:
    print("No")