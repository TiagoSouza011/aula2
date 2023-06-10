numero1= int(input("Entre com o primeiro número:"))
numero2= int(input("Entre com o segundo número:"))
numero3= int(input("Entre com o terceiro número:"))


if numero1>numero2 and numero3:
    maior_numero=numero1
if numero2>numero1 and numero3:
    maior_numero=numero2
if  numero3>numero1 and numero2:
    maior_numero=numero3




    print("o maior número é",maior_numero)