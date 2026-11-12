n = int(input())
yozuvlar = []
for _ in range(n):
    name, score = input().split()
    yozuvlar.append(name + ":" + score)
f = open("task15.txt", "w")
for y in yozuvlar:
    f.write(y + "\n")
f.close()
f = open("task15.txt", "r")
balllar = []
for qator in f.readlines():
    qator = qator.strip()
    if qator:
        name, score = qator.split(":")
        balllar.append(int(score))
f.close()
print(len(balllar))
print(f"{sum(balllar) / len(balllar):.2f}")
print(max(balllar))