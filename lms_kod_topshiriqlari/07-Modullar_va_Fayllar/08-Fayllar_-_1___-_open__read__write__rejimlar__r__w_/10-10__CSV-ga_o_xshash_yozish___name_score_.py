n = int(input())
yozuvlar = []
for _ in range(n):
    name, score = input().split()
    yozuvlar.append(name + "," + score)
f = open("task10.txt", "w")
for y in yozuvlar:
    f.write(y + "\n")
f.close()
f = open("task10.txt", "r")
kontent = f.read()
f.close()
print(kontent, end="")