
n = int(input().strip())
users = []
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})

a = users[0]

for user in users:
    if len(user['tags']) > len(a['tags']):
        a = user
        
print(a['username'])