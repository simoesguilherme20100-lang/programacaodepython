import statistics

clientes = [
{"Idade": 45, "Limite": 12691, "Meses_cliente": 39, "Taxa_utilizacao": 0.061},
{"Idade": 49, "Limite": 8256, "Meses_cliente": 44, "Taxa_utilizacao": 0.105},
{"Idade": 51, "Limite": 3418, "Meses_cliente": 36, "Taxa_utilizacao": 0},
{"Idade": 40, "Limite": 3313, "Meses_cliente": 34, "Taxa_utilizacao": 0.76},
{"Idade": 40, "Limite": 4716, "Meses_cliente": 21, "Taxa_utilizacao": 0},
{"Idade": 44, "Limite": 4010, "Meses_cliente": 36, "Taxa_utilizacao": 0.311},
{"Idade": 51, "Limite": 34516, "Meses_cliente": 46, "Taxa_utilizacao": 0.066},
{"Idade": 32, "Limite": 29081, "Meses_cliente": 27, "Taxa_utilizacao": 0.048},
{"Idade": 37, "Limite": 22352, "Meses_cliente": 36, "Taxa_utilizacao": 0.113},
{"Idade": 48, "Limite": 11656, "Meses_cliente": 36, "Taxa_utilizacao": 0.144},
{"Idade": 42, "Limite": 6748, "Meses_cliente": 31, "Taxa_utilizacao": 0.217},
{"Idade": 65, "Limite": 9095, "Meses_cliente": 54, "Taxa_utilizacao": 0.174},
]

# list_compressions 

idades  =  [c['Idade'] for c  in clientes]
limites  =  [c ['Limite'] for c in clientes]
meses =  [c ['Meses_cliente'] for c in clientes]
utilizacoes  =  [c ['Taxa_utilizacao'] for c in clientes]


def resumo(nome, dados):
    print(nome)
    print('Media', statistics.mean(dados))
    print('Mediana', statistics.median(dados))
    print('Desvio', statistics.stdev(dados))
    moda  =  statistics.multimode(dados)
    c  =  set(dados)
    if len(c) != len(moda):
        print('Modas:', moda)   
        
    else:    
        print("Não tem moda")
    
    
  
         

# print('idades', idades)
# print('Limites', limites)
# print('meses', meses)
# print('Utilização do CC', utilizacoes)
    

resumo('idades', idades) 
print('---' * 10)
resumo('limites', limites)  
print('---' * 10)
resumo('meses', meses)   
print('---' * 10)
resumo('Taxa de utilização ', utilizacoes)  