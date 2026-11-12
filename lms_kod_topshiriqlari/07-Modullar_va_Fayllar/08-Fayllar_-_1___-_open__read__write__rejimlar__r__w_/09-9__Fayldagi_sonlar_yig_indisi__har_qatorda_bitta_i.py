n = int(input())
sonlar = []
for _ in range(n):
    sonlar.append(input())
f = open("task9.txt", "w")
for s in sonlar:
    f.write(s + "\n")
f.close()
f = open("task9.txt", "r")
jami = 0
for qator in f.readlines():
    jami += int(qator.strip())
f.close()
print(jami)