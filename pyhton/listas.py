notas =[7.9, 9.7, 8.2]
lista= [26, "vivi", 3.48747, False]
lista_de_listas = [10, [20, 40]]

print(lista[0], lista[1], lista[-1])


lista = [10, 20, 30, 40, 50]
    #do 0 ao 3; do 0 ate o final; do 2 ao 5 de 2 em 2
print(lista[0:3], lista[0:], lista[2:5:2])
print("tamanho da lista", len(lista))

#percorre a lista
for i in lista:
    print(i)

for i in range(len(lista)):
    print(lista[i])
lista = [1, 2, 3, 4, 5, 6, 7, 8]
print("antes do apppend", lista)
lista.append(3)
print("depois do append", lista)
lista.insert(2, 10)
print("depois do insert", lista)
lista2 = [48,67,3829]
lista.extend(lista2)
print("Depois do extend", lista)
lista.pop()
print("lista apos o pop", lista)
lista.pop(0)
print("lista apos o pop", lista)
lista.remove(2)
print("lista apos o remove", lista)
lista.count(2)
print("quantidade de 2 na lista")
lista.index(3)
print("indice do elemento 3")
lista.sort(reverse=True)
print(lista)

print(len(lista))
print(sum(lista))
print(min(lista))
print(max(lista))
