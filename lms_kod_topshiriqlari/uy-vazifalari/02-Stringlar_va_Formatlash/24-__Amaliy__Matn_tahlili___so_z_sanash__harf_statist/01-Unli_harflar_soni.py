s = input().lower()
unli = "aeiou"
son = 0
for x in s:
    if x in unli:
        son += 1
print(son)