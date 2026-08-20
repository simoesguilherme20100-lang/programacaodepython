def display(): 
    print('SISTEMA DE CALCULO TRABALHISTA')
    
    
# calcule o valor hora do trabalhador


def valor_hora(salario, carga):
    return salario / carga 



# calcule o valor da hora extra 


def calculo_v_extra(valor_hora):
    return valor_hora * 1.5


# calcule quantidade valor que ele vai ganhar de extra


def calculo_valor_extra(quantidade, cv_extra):
    return cv_extra  * quantidade



def salario_total(salario, calculo_valor_extra):
    return salario + calculo_valor_extra


# calcule i salario total ...     


def sistema_calculo_horas():
    display()
    nome =  input('Nome do colaborador: ')
    salario =  float(input('Salário: '))
    carga =  float(input('Carga: '))
    v_hora = valor_hora(salario, carga)
    print('Valor hora do(a)', nome, round(v_hora,2)) 
    print('****' *  10)
    cal_extra  = calculo_v_extra(v_hora)
    print('O valor da hora extra é', round(cal_extra,2)) 
    print('****' *  10)  
    q =  float(input('Quantidade de extra: '))
    total_receber_extra =  calculo_valor_extra(10, cal_extra)
    print('Hora extra  R$', round(total_receber_extra,2))
    print('****' *  10)  
    total = salario_total(salario, total_receber_extra)
    print('Salário total: ', round(total,2))


sistema_calculo_horas()