s = input()
j = sum(1 for i in s if i.isdigit() and int(i) % 2 == 0)
print(j)