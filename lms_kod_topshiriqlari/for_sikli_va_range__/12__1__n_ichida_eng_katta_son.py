n = int(input())
son = 0
for i in range(1, n + 1):
    if i > son:
        son = i
print(son)