

# media
vendas =  [200,5550,280,310,520,5000,150, 150,150]
media =  sum(vendas) / len(vendas)
print(media)

# mediana
ordenada = sorted(vendas)
print(ordenada)
mediana = ordenada[3]
print(mediana)

# moda
c  =  set(vendas)

if len(vendas) == len(c):
    print('Não tem moda')
else:
    l = []
    for n in vendas:
        l.append(n)
        x  = l.count(n)
        if x > 1:
            print(x)
           
    print('Tem moda')  