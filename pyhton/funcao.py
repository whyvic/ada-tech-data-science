def saudacao(nome, curso='python'):

    print(f'seja bem vindo, {nome}')
    print(f'ola é um prazer ter voce fazendo parte desse curso de {curso}')
saudacao('vivi')

def soma (num1, num2):
    return num1+num2
resultado = soma (4,8)
print(resultado)

def calculadora(num1,num2, operacao='+'):
    if(operacao == '+'):
        return num1+num2
    elif operacao == '-':
        return num1-num2
resultado = calculadora(10,20, '=')
print(resultado)