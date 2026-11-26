name = input().strip()
phone = input().strip()
query_name = input().strip()
kontaktlar = {name: phone}
with open("pbook1.txt", "w", encoding="utf-8") as f:
    for k, v in kontaktlar.items():
        f.write(k + "=" + v + "\n")
kitob = {}
with open("pbook1.txt", "r", encoding="utf-8") as f:
    for qator in f:
        qator = qator.rstrip("\n")
        if qator:
            k, v = qator.split("=", 1)
            kitob[k] = v
if query_name in kitob:
    print(kitob[query_name])
else:
    print("NOTFOUND")