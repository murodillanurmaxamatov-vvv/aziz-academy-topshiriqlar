w = input().split()

a = [i.lower() for i in w if i.lower().startswith('a')]

print(*a if a else ["BO'SH"])