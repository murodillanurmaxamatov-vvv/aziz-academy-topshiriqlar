n = int(input())

s = []

for _ in range(n):
    name, score = input().split()
    s.append({"name": name, "score": int(score)})
    
b = s[0]

for i in s[1:]:
    if i["score"] > b["score"]:
        b = i
    elif i["score"] == b["score"] and i["name"] < b["name"]:
        b = i
        
print(b["name"], b["score"])