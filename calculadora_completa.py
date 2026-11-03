# Sistema de calculadora para realizar operações matemáticas e conversão de unidades.
# Author: Marco Salco

import math

#Funções matemáticas
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y
def multiplicacao(x, y):
    return x *y 

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    else:
        return x / y
    
def raiz_quadrada(x):
    if x < 0:
        return "Erro: Raiz quandrada de número negativo!"
    else:
        return math.sqrt(x)
    
def potencia(x, y):
    return x ** y

def logaritmo(x):
    if x <= 0:
        return "Erro: Logaritmo de número não positivo!"
    else:
        return math.log(x)
    
def seno(x):
    return math.sin(x)

def cosseno(x):
    return math.cos(x)

def tangente(x):
    return math.tan(x)

#Funções de conversão de unidades
def comprimento(x, unidade):
    if unidade == "km":
        return x * 1000
    elif unidade == "m":
        return x
    elif unidade == "cm":
        return x / 100
    elif unidade == "mm":
        return x / 1000
    else:
        return "Erro: Unidade inválida!"
    
def massa(x, unidade):
    if unidade == "kg":
        return x
    elif unidade == "g":
        return x / 1000
    elif unidade == "mg":
        return x / 1000000
    else:
        return "Erro: Unidade inválida!"
    
def tempo(x, unidade):
    if unidade == "s":
        return x
    elif unidade == "min":
        return x / 60
    elif unidade == "h":
        return x / 3600
    else:
        return "Erro: Unidade inválida!"
    
while True:
    print("Calculadora em Python")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Raiz quadrada")
    print("6. Potenciação")
    print("7. Logaritmo")
    print("8. Seno")
    print("9. Cosseno")
    print("10.Tangente")
    print("11. Conversão de unidades")
    print("12. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", soma(num1, num2))

    elif escolha == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: " , subtracao(num1 , num2))

    elif escolha == "3":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", multiplicacao(num1, num2))

    elif escolha == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        print("Resultado: ", divisao(num1, num2))
    elif escolha == "5":
        num = float(input("Digite um número: "))
        print("Resultado:", raiz_quadrada(num))

    elif escolha == "6":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado: ", potencia(num1, num2))

    elif escolha == "7":
        num = float(input("Digite um número:"))
        print("Resultado:", logaritmo(num))

    elif escolha == "8":
        num = float(input("Digite um ângulo em radianos: "))
        print("Resultado: ", seno(num))

    elif escolha == "9":
        num = float(input("Digite um ângulo em radianos: "))
        print("Resultado: ", cosseno(num))

    elif escolha == "10":
        num = (input("Digite um ângulo em radianos: "))
        print("Resultado: ", tangente(num))

    elif escolha == "1":
        print("Conversão de unidades")
        print("1. Comprimento")
        print("2. Massa")
        print("3. Tempo")
        escolha_unidade = input("Escolha uma opção: ")
        if escolha_unidade == "1":
            num = float(input("Digite um valor: "))
            unidade = input("Digite a unidade (km, m, cm, mm): ")
            print("Resultado: ", comprimento(num, unidade))
        elif escolha_unidade == "2":
            num = float(input("Digite um valor: "))
            unidade = input("Digite a unidade (kg, g, mg): ")
            print("Resultado: ", massa(num, unidade))
        elif escolha_unidade == "3":
            num = float(input("Digite um valor: "))
            unidade = input("Digite a unidade (s, min, h): ")
            print("Resultado: ", tempo(num, unidade))

    elif escolha == "12":
        print("Saindo da calculadora...")
        break
    else:
        print("Opção inválida. Tente novamente!")
        

    

