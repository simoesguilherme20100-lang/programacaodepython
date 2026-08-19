VENDAS = {
'SETOR1':{
'MÊS 1':[150,200,300]},
'SETOR2':{
'MÊS 2':[300,250,300]},
'SETOR3':{
'MÊS 3':[15,20,300]},
'SETOR4':{
'MÊS 4':[150,2000,300000],
}
}



# Você foi contratado para verificar qual setor vendeu mais, 



setor_1 = VENDAS['SETOR1']['MÊS 1']
print(setor_1)
setor_2 = VENDAS['SETOR2']['MÊS 2']
print(setor_2)
setor_3 = VENDAS['SETOR3']['MÊS 3']
print(setor_3)
setor_4 = VENDAS['SETOR4']['MÊS 4']
print(setor_4)

setores = [setor_1, setor_2, setor_3, setor_4]

todas_vendas = []
todas_vendas += (setor_1, setor_2,setor_3, setor_4)
maior_venda =  max(todas_vendas)
setor_q_mais_vendeu = todas_vendas.index(maior_venda)
print('O SETOR QUE MAIS VENDEU - ', setores[setor_q_mais_vendeu])

soma  =  sum(todas_vendas)/len(todas_vendas)
print('R$ total ', soma)

print(maior_venda)