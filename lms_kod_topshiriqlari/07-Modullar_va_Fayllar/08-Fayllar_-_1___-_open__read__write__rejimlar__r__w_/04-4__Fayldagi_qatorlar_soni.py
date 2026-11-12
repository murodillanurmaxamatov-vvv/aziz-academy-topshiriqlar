n = int(input())
qatorlar = []
for _ in range(n):
    qatorlar.append(input())
f = open("task4.txt", "w")
for q in qatorlar:
    f.write(q + "\n")
f.close()
f = open("task4.txt","r")
print(len(f.readlines()))
f.close()
