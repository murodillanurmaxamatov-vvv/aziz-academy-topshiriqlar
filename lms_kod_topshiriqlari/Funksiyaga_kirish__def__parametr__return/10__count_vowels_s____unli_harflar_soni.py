def unli(s):
    v = "aeiouAEIOU"
    count = 0
    for i in s:
        if i in v:
            count += 1
    return count

s = input()
print(unli(s))