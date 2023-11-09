for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)
soma = 0
for i in range(1,4):
    nota = float(input(f"informe sua nota {i}:"))
    soma += nota
    media = soma/3
print("sua media é:", media)