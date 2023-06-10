numero1= int(input("Entre com o primeiro número:"))
numero2= int(input("Entre com o segundo número:"))


if numero1 == numero2:
    print("numeros iguais")


else:
    if numero1 > numero2:
        print("foi validado o item abaixo: \n")
        print (numero1)
    else:
            print("o maior número é o item abaixo: \n")
            print (numero2)


print("os resultados foram mostrados")