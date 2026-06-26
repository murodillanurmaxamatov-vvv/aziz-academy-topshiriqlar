s1 = input().strip().lower().split()
s2 = input().strip().lower().split()

a = set(s1)
b = set(s2)
c = (a | b)
print(len(c))