# Sistema conciso de conversor de moedas
# Autor: Marco Salco


import requests

# Função para pegar a cotação da moeda
def pegar_cotacao_moeda(moeda_origem, moeda_destino):
    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
    requisicao = requests.get(link)
    cotacao = requisicao.json()[f"{moeda_origem}{moeda_destino}"]["bid"]
    return cotacao

# Função principal do conversor de moedas
def conversor_moeda():
    print("Conversor de Moeda")
    print("1. Real para Dólar")
    print("2. Real para Euro")
    print("3. Dólar para Real")
    print("4. Euro para Real")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    # Real para Dólar
    if opcao == "1":
        valor = float(input("Digite o valor em Real: "))
        cotacao = pegar_cotacao_moeda("BRL", "USD")
        resultado = valor / float(cotacao)
        print(f"{valor} BRL é igual a {resultado: .2f} USD")

    # Real para Euro
    elif opcao == "2":
        valor = float(input("Digite o valor em Real"))
        cotacao = pegar_cotacao_moeda("BRL", "EUR")
        resultado = valor / float(cotacao)
        print(f"{valor} BRL é igual a {resultado: .2f} EUR")

    # Dólar para Real
    elif opcao == "3":
        valor = float(input("Digite o valor em Dólar: "))
        cotacao = pegar_cotacao_moeda("USD", "BRL")
        resultado = valor * float(cotacao)
        print(f"{valor} USD é igual a {resultado: .2f} BRL")

    # Euro para Real
    elif opcao == "4":
        valor = float(input("Digite o valor em Euro: "))
        cotacao = pegar_cotacao_moeda("EUR", "BRL")
        resultado = valor * float(cotacao)
        print(f"{valor} EUR é igual a {resultado: .2f} BRL")

    elif opcao == "5":
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")

while True:
    conversor_moeda()

    
