while True:
    p =  input('Deseja acessar p banco? ')
    saldo = [100]
    extrato = []
    while p == 'sim':
        for n in range(3):
            senha  =  input('Senha:')
            if senha  == '123':
                print('Bem vindo ao banco X')
                escolha =  input('1 saque  2 deposito 3 extrato 4 sair')  
                if escolha == '1':
                    s =  sum(saldo)
                    saque = float(input('Saque R$: '))
                    if saque > s:
                        print('Saldo insuficiente ... ')
                    else:     
                            r  =  s - saque
                            print('Valor em conta', r)
                            saldo[0] = r
                            extrato.append(-saque)
                            
                elif escolha == '2':
                    s =  sum(saldo)
                    deposito = float(input('Saque R$: '))
                    r  =  s + deposito
                    print('Valor em conta', r)
                    saldo[0] = r
                    extrato.append(deposito)               
                elif escolha == '3':
                    print(extrato)            
                elif escolha == '4':
                    print('Obrigada volte sempre!!!')
                    exit()      
        print('senha bloqueada ... entre em contato ')            
        break

def sistema():
    p = float(input('>>>'))
    a = float(input('>>>'))    
    mostrar_imc(p,a)    
    
sistema()    

