import timeit
import numpy as np


# def soma1 ():
#     lista =  list(range(1,2000))
#     print(lista)
#     return lista


# soma1()
# time = timeit.timeit(soma1, number=10)
# print('função1', time)


lista =  list(range(1,2000))
def soma():
    aleatorio1 =  np.array(lista)
    # print(aleatorio1)
    print(aleatorio1)
    return aleatorio1


time = timeit.timeit(soma, number=10)
print('função2', time)

