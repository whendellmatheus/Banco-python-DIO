menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print ("Depósito realizado com Sucesso!")

        else: 
            print("Operação falhou, o valor informado é inválido. Tente Novamente!")    

    elif opcao == "2":
        valor = float(input("informe o valor a ser sacado: "))

        excede_saldo = valor > saldo

        excede_limite =  valor > limite

        excede_limite_saque = numero_saques > LIMITE_SAQUES

        if excede_saldo:
            print("Operação Falhou! Você não possui saldo suficiente.")

        elif excede_limite:
            print("Operação Falhou! Operação excede o valor limite para saques.")

        elif excede_limite_saque:
            print ("Operação Falhou! Número máximo de saques excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Operação falhou, o valor informado é inválido. Tente Novamente!")

    elif opcao == "3":
        
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================")

    elif opcao == "4":
        print("Sair")
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada")
