
n = int(input().strip())
data = {'courses': []}
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    data['courses'].append({'name': name, 'students': students})

total = 0

for course in data['courses']:
    total += len(course['students'])
    
print(total)
