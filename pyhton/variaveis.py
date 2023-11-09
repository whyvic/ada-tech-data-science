#inicializando variavel e construindo uma calculadora
#conhecendo os tipos primitivos em python
idade = '26'
nome = "vitoria"
altura = 1.77
profissao = "estudante"

print(f'Meu nome é: {nome} \nMinha idade é: {idade} \nMinha altura é: {altura} \nE sou {profissao}')

print(f'o tipo de {idade}', type(idade))
intIdade = int(idade)
print(f'o tipo de {intIdade} convertido para inteiro', type(intIdade))

linguagem = input("Qual a linguagem de programação que voce esta estudando? ")
print("A linguagem que voce esta estudando é: ", linguagem)

num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
print("soma: ", num1+ num2)
print("subtração: ", num1- num2)
print("multiplicação: ", num1* num2)
print("divisao: ", num1/ num2)
print("divisao inteira: ", num1// num2)
print("resto da divisao: ", num1% num2)
print("potencia: ", num1** num2)
"""
"""