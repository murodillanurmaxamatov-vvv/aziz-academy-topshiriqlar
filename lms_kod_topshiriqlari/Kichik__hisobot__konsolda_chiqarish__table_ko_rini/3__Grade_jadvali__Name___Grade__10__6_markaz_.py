n = int(input())

s = []

for _ in range(n):
    name, a = input().split()
    a = int(a)
    
    if 90 <= a <= 100:
        grade = 'A'
    elif 80 <= a <= 89:
        grade = "B"
    elif 70 <= a <= 79:
        grade = "C"
    elif 60 <= a <= 69:
        grade = 'D'
    else:
        grade = 'F'
    
    s.append((name, grade))
    
print(f"{'Name':10} | Grade")
print(f"{'-'*10}+------")

for name, grade in s:
    print(f"{name:<10} |   {grade}")