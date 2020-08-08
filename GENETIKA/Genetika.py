DNK = input('Шото: ')

DNK_S1 = DNK.split()
DNK_S2 = []

print(DNK_S1)

for j in DNK_S1:
    if j == 'а':
        j = 'т'
        DNK_S2.append(j)
    else:
        DNK_S2.append(j)

print(DNK_S2)