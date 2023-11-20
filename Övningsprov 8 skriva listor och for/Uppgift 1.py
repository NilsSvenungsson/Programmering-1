lista = [2, 3, 2, 4, 1]


lista[1] = 5

lista[4] = 6

lista.append(4)

medel = sum(lista) / len(lista)
print("medel:", medel)

lista.sort()
print(lista)
