s = input().split()
c = sum(1 for i in s if i.lower().startswith("a"))
print(c)