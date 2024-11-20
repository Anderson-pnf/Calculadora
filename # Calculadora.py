# Calculadora
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def divisao(x, y):
    if x == 0 or y == 0:
        return "Impossivel fazer este calculo..."    
    return x / y

def multiplicacao(x, y):
    return x * y

def calculadora():

    while True:
        opcao = int(input('''Escolha uma das opções: 
1 - Soma
2 - Subtração
3 - Divisao
4 - Multiplicação
5 - Sair
>>> '''))
        if opcao == 5:
            print("Estamos saindo ...")
            break
        if opcao not in [1,2,3,4]:
            continue
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite um numero: "))
        if opcao == 1:
            print(soma(num1,num2))
        if opcao == 2:
            print(subtracao(num1,num2))
        if opcao == 3:
            print(divisao(num1,num2))
        if opcao == 4:
            print(multiplicacao(num1,num2))
        

calculadora()
