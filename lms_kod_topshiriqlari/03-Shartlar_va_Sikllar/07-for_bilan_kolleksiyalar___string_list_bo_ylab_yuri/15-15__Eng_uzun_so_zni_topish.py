s = input().split()
longest = ""
for i in s:
    if len(i) > len(longest):
        longest = i
print(longest)