menu = """

======================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
======================

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        print("Depósito")
        valor = float(input("Digite o valor do deposito: "))
        if valor > 0:
            saldo += valor
            print("Valor depositado com sucesso!")
            extrato += f' Deposito R$ {valor:.2f}\n'
        else:
            print("Valor insuficiente")


    elif opcao == "s":
        print("Saque")
        valor = float(input("Digite o valor do saque: "))

        limite_diario = numero_saques >= LIMITE_SAQUES

        limite_saque = valor > limite

        valor_insuficiente = valor > saldo

        if limite_diario:
            print("Limite diário de saques atingido! ")

        elif limite_saque:
            print("Atingiu seu limite de saque! ")

        elif valor_insuficiente:
            print("Não será possível sacar por falta de saldo! ")

        else:
            saldo -= valor
            numero_saques +=1
            print("Valor sacado com sucesso!")
            extrato += f' Saque R$ {valor:.2f}'


    elif opcao == "e":
        print("EXTRATO".center(50, "="))
        print(f"Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSeu saldo atual {saldo:.2f}")
        print("=".center(50, "="))
       

    elif opcao == "q":
        break

    else:
        print("Opção invalida")



        



