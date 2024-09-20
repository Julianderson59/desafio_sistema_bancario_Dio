saldo = 1500
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

menu = """
    =============MENU============
    
    1-Deposito
    2-Sacar
    3-Extrato
    0-Sair

"""
print(menu)

def realizar_deposito(valor):
        global saldo, extrato
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"

def realizar_saque(valor):
    global saldo, limite, numero_saque, extrato
    if numero_saque >= limite_saque:
        print("Limite de saque atingido")
    elif valor > saldo:
        print("Saldo insuficiente")
    elif limite < valor:
        print("Seu saque é maior que o limite permitido")
    else:
        saldo -= valor
        numero_saque += 1
        extrato += f"Saque: R${valor:.2f}\n"

def exibir_extrato():
    print("Seu extrato:")
    print(extrato)
    print(f"Seu saldo é: R${saldo:.2f}\n")

while True:

    opcao = int(input("Informe o serviço do menu: "))

    if(opcao == 1):
        deposito = float(input("informe o valor que deseja depositar: "))
        if(deposito > 0):
            realizar_deposito(deposito)
    elif(opcao ==2):
        sacar = float(input("Informe a valor que deseja sacar: "))
        if sacar > 0:
            realizar_saque(sacar)
    elif(opcao ==3):
        exibir_extrato()
    elif(opcao == 0):
        break