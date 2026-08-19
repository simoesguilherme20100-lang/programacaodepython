pe =  input('Deseja acessar o banco? ')


while pe  == 'sim':
    senha  =  input('Senha')
    if senha  == '123':
        print('banco X')
        print('''Menu:
            
            1 - saque
            2 - deposito
            3 - extrato
            4 -  sair 
            
            
            
            ''')
        op =  input('escolha a operação: ')
        if  op == '1':
            pe =  input('Deseja acessar o banco? ')
            pass
    else:
        print('Deseja coninuar?')            




# SISTEMA DE BANCO

# Variáveis
saldo = 1000.00

# Lista para guardar as movimentações
extrato = []

# Dicionário com os dados da conta
conta = {
    "titular": "Cliente",
    "numero": 12345
}

# Loop principal
while True:
    print("\n===== SISTEMA DE BANCO =====")
    print("1 - Ver extrato")
    print("2 - Fazer depósito")
    print("3 - Fazer saque")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # Ver extrato
    if opcao == "1":
        print("\n--- EXTRATO ---")
        print("Titular:", conta["titular"])
        print("Conta:", conta["numero"])
        print(f"Saldo: R$ {saldo:.2f}")

        if len(extrato) == 0:
            print("Nenhuma movimentação.")
        else:
            print("Movimentações:")
            for movimentacao in extrato:
                print("-", movimentacao)

    # Fazer depósito
    elif opcao == "2":
        deposito = float(input("Digite o valor do depósito: R$ "))

        if deposito > 0:
            saldo = saldo + deposito
            extrato.append(f"Depósito: + R$ {deposito:.2f}")
            print(f"Depósito realizado! Novo saldo: R$ {saldo:.2f}")
        else:
            print("Valor de depósito inválido.")

    # Fazer saque
    elif opcao == "3":
        saque = float(input("Digite o valor do saque: R$ "))

        if saque > 0 and saque <= saldo:
            saldo = saldo - saque
            extrato.append(f"Saque: - R$ {saque:.2f}")
            print(f"Saque realizado! Novo saldo: R$ {saldo:.2f}")
        elif saque > saldo:
            print("Saldo insuficiente!")
        else:
            print("Valor de saque inválido.")

    # Sair
    elif opcao == "4":
        print("Obrigado por utilizar nosso banco!")
        print("Até logo!")
        break


    # Opção inválida
    else:
        print("Opção inválida! Tente novamente.")


pe =  input('Deseja acessar o banco? ')
saldo  =  [1000]
extrato =  []
movimen = 0
while pe  == 'sim':
    for x  in range(3):      
        senha  =  input('Senha')
        if senha  == '123':
            print('banco X')
            op =  input('''Menu:
                
                1 - saque
                2 - deposito
                3 - extrato
                4 -  sair 
                    
                
                ''')
            
        
            if  op == '1':
                
                valor_saque  =  float(input('Valor R$ saque: '))
                if valor_saque >  saldo[0]:
                    print('Saldo insuficiente')
                    pe =  input('Deseja acessar o banco? ')
                    
                else:     
                    sal =  sum(saldo)
                    s  = sal -  valor_saque
                    saldo[0] =  s            
                    extrato.append(- valor_saque)
                    print('valor em conta', saldo)         
                    movimen = s
                    pe =  input('Deseja acessar o banco? ')
            
            elif op == '2':
                valor_dep  =  float(input('Valor R$ deposito: '))
                if valor_dep and movimen:
                    s  = movimen +  valor_dep
                    saldo[0] =  s
                    extrato.append(valor_dep)
                    print('valor em conta', saldo)
                else:
                    s =  sum(saldo) + valor_dep
                    extrato.append(valor_dep)
                    print('valor em conta', s)
                    pe =  input('Deseja acessar o banco? ')            
                
            elif op ==  '3':
                print(extrato)
                # extrato    
                
            elif op == '4':
                print('Obrigada volte sempre! ')
                exit()    
                
        else:
            print('Senha incorreta ... ')            
    else:
        print('senha bloqueada ... ')
        exit()




pe =  input('Deseja acessar o banco? ')
saldo  =  [1000]
extrato =  []
movimen = 0
while pe  == 'sim':
    for x  in range(3):      
        senha  =  input('Senha')
        if senha  == '123':
            print('banco X')
            op =  input('''Menu:
                
                1 - saque
                2 - deposito
                3 - extrato
                4 -  sair 
                    
                
                ''')
            
        
            if  op == '1':
                
                valor_saque  =  float(input('Valor R$ saque: '))
                if valor_saque >  saldo[0]:
                    print('Saldo insuficiente')
                    pe =  input('Deseja acessar o banco? ')
                    
                else:     
                    sal =  sum(saldo)
                    s  = sal -  valor_saque
                    saldo[0] =  s            
                    extrato.append(- valor_saque)
                    print('valor em conta', saldo)         
                    movimen = s
                    pe =  input('Deseja acessar o banco? ')
            
            elif op == '2':
                valor_dep  =  float(input('Valor R$ deposito: '))
                if valor_dep and movimen:
                    s  = movimen +  valor_dep
                    saldo[0] =  s
                    extrato.append(valor_dep)
                    print('valor em conta', saldo)
                else:
                    s =  sum(saldo) + valor_dep
                    extrato.append(valor_dep)
                    print('valor em conta', s)
                    pe =  input('Deseja acessar o banco? ')            
                
            elif op ==  '3':
                print(extrato)
                # extrato    
                
            elif op == '4':
                print('Obrigada volte sempre! ')
                exit()    
                
        else:
            print('Senha incorreta ... ')            
    else:
        print('senha bloqueada ... ')
        exit()






