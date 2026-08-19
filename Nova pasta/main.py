


dados = [10,20,30,10]


op = input('''Escolha a operação
           
           1 - Mostra o dado
           2 - Alterar o dado
           3 - Coletando Dados
           4 - Soma de Dados
           5 - Localizar um Registro
           
           ''')



if op == '1':
    print(dados)
elif op == '2':
    print(dados)
    valor_add  =  int(input('Valor que vai inserir:  '))   
    tirar_valor  =  int(input('Valor que vai remover:  '))  
    posi_v_rem =  dados.index(tirar_valor)
    dados[posi_v_rem] =  valor_add
    print(dados)
elif op == '3':
    ex1 = int(input('Valor experimento:  '))     
    ex2 = int(input('Valor experimento:  '))  
    ex3 = int(input('Valor experimento:  '))  
    dados.extend([ex1,ex2, ex3])
    print(dados)
elif op == '4':
    soma =  sum(dados)
    print(soma)
    
elif op == '5':
    valor_loc =  int(input('Localize: '))
    if valor_loc in dados:
        print('Valor localizado: ', valor_loc)
        po = dados.index(valor_loc)
        print('Sua posição é',po)
    else:
        print('ESSE VALOR NÃO EXISTE NESSA FERQUENCIA')            


     
    
# - Mostra o dado;
# - Alterar o dado;
# - Coletando Dados de Experimentos
# - Analisando a Soma de Dados de Vendas
# - Localizar um Registro no Conjunto de Dados







# finito = 
for x in range(3):
    login  = input('login: ')
    senha =  input('senha: ')
    if login == 'b' and senha =='1':
        print('Produtos>')
        produ = ['uva', 'pera', 'manga ']
        print(produ)
        break
else:
    print('bloquedo ...')    


    

lista  =  [1,2,3]
tupla  =  (4,5,6)
d = {
    'a':200,
    'b':500,
    'c': 1000
    }
for n in d.keys():
    print(n)    







pe =  input('Deseja acessar o banco? ')


while pe  == 'sim':
    print('banco X')
    print('''Menu:
          
          1 - saque
          2 - deposito
          3 - extrato
          4 -  sair 
          
          
          
          ''')
op =  input('escolha a operação: ')
if  op == '1':
               




