menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
saques_realizados = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao.lower() == 'd':
        valor_deposito = float(input("Insira o valor que deseja depositar: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"\nDepósito de R$ {valor_deposito:.2f} realizado com sucesso!")

        else:
            print("\nA operação falhou. O valor do depósito deve ser maior que 0.")
    
    elif opcao.lower() == 's':
        valor_saque = float(input("Insira o valor que deseja sacar: "))

        # Verificar as condicoes de saque:
        excedeu_saldo = valor_saque > saldo
        excedeu_saques_diarios = saques_realizados >= LIMITE_SAQUES
        excedeu_limite_por_saque = valor_saque > limite
        saque_negativo_ou_nulo = valor_saque <= 0

        if excedeu_saldo:
            print(f"\nA operação falhou. Você não tem saldo suficiente. Seu saldo atual é de R$ {saldo:.2f}.")
        
        elif excedeu_limite_por_saque:
            print(f"\nA operação falhou. O limite máximo por saque é de R$ {limite:.2f}.")
        
        elif excedeu_saques_diarios:
            print(f"\nA operação falhou. Você atingiu o número máximo de {LIMITE_SAQUES} saques diários.")

        elif saque_negativo_ou_nulo:
            print(f"\nA operação falhou. O valor do saque deve ser maior que 0.")
            
        else:
            saldo -= valor_saque
            saques_realizados += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print(f"\nSaque de R$ {valor_saque:.2f} realizado com sucesso!")

    elif opcao.lower() == 'e':
        print("\n=============== EXTRATO ===============")

        if len(extrato) > 0:
            print(extrato)
        
        else:
            print("Não foram realizadas movimentações.\n")
        
        print(f"\nSaldo atual da conta: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao.lower() == 'q':
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada conforme as opções do menu abaixo:")