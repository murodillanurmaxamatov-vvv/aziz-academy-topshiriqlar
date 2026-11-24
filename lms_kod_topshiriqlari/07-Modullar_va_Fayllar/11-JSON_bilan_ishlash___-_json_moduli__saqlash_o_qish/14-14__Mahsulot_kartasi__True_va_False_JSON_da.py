import json

# Kodingizni shu yerga yozing
nom = input()
narx = int(input())
javob = input()
mahsulot = {"nom": nom, "narx": narx, "mavjud": javob=="ha"}
print(json.dumps(mahsulot, ensure_ascii=False))