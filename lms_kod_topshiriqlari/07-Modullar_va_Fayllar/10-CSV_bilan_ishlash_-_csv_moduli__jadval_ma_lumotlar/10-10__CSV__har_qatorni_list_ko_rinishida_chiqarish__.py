import csv
n = int(input())
rows = []
for _ in range(n):
    rows.append(input().split())
with open("c10.csv", "w", newline="") as f:
    yozgich = csv.writer(f)
    for row in rows:
        yozgich.writerow(row)
with open("c10.csv", "r", newline="") as f:
    for row in csv.reader(f):
        print(row)