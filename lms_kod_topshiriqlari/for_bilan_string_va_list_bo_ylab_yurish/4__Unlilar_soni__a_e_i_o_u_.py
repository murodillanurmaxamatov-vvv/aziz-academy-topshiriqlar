s = input()
unli = "aeiou"
son = 0
for i in s:
    if i in unli:
        son += 1
print(son)