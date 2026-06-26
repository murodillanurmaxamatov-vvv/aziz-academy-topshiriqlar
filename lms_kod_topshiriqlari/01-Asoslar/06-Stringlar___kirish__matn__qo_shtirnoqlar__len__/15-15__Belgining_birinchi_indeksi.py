x = input()
ch = input()
words = x.split()
pos = -1
for i in range(len(words)):
    if ch in words[i]:
        pos = i
print(pos)