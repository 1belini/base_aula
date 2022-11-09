def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Soma: ",x+y)

def subtracao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Subtracao: ",x-y)

def multiplicacao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Multiplicacao: ",x*y)

def divisao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Divisao: ",x/y)

def pula():
    print("")

def header():
    print("=========================")
    print("= CALCULADORA AMS'S DAY =")
    print("=========================")
opcao=1

while opcao:
    header()
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")

    opcao = int(input("Opção: "))

    if(opcao==1):
        soma()
        pula()
    if(opcao==2):
        subtracao()
        pula()
    if(opcao==3):
        multiplicacao()
        pula()
    if(opcao==4):
        divisao()
        pula()
