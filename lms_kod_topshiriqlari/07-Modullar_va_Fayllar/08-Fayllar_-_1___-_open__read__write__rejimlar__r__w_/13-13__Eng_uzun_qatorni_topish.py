n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
f = open("task13.txt", "w")
for q in qatorlar:
    f.write(q + "\n")
f.close()
f = open("task13.txt", "r")
eng_uzun = None
for qator in f.readlines():
    qator = qator.rstrip("\n")
    if eng_uzun is None or len(qator) > len(eng_uzun):
        eng_uzun = qator
f.close()
print(eng_uzun)