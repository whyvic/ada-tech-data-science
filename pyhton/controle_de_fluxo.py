#verificando maior idade
idade = int(input("diga sua idade: "))
if idade >= 18:
    print("voce é maior de idade")
else:
    print("voce é menor de idade")

#verificando media 
media = float(input("digita a nota: "))
if media >= 7:
    print("voce passou de ano")
elif media >=5:
    print("voce esta de recuparação ")
else:
    print("voce foi reprovado")
#verificação de media e presenca

media = int(input("digite a media: "))
presenca = int(input("digite a presença: "))
if media >= 7 and presenca >= 70:
    print("aprovado")
else:
    print("reprovado")