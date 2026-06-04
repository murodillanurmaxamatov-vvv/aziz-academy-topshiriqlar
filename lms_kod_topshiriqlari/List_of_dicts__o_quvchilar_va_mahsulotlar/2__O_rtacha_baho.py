n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
avg = sum(s['score'] for s in students) / n
print(avg)