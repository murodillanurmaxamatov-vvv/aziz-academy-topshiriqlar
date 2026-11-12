n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
f = open("task14.txt", "w")
for q in qatorlar:
    f.write(q + "\n")
f.close()
f = open("task14.txt", "r")
for qator in f.readlines():
    if qator.strip() != "":
        print(qator.rstrip("\n"))
f.close()
