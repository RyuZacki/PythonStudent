
a = ["Жопа", "Пися", "Гавно"]

print(len(a))

b = "Жопа"
for i in a:
    if i == b:
        a.append("Привет")

print(len(a))