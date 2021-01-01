
a = ["Жопа", "Пися", "Гавно"]

print("Жопа" in a)

b = "Жопа"
for i in a:
    if i == b:
        a.append("Привет")

print(len(a))