
#permitir que um professor informe as notas de seus alunos
#Ele tem 6 alunos
#Exibir as notas em uma matriz 3x2
#Exibir o desvio padrão

import numpy as np
alunos = np.arange(6).reshape((3,5))
print(alunos)




# import numpy as np
# # r1= np.arange(15).reshape((3,5))
# # print(r1)
# # r2 = r1.reshape((3,5))
# # print(r2)


# m1 =np.array ([
#     [1,2]
#     [3,4]
# ])

# m2 = np.array([
#     [1,1],
#     [1,1]
# ])
# print(m1+m2)


# k = np.array([
#     [4,5]
#     [6,1]
#     [7,4]
# ])
# print(k)
# linha1 = k[0,:]
# print (linha1)
# eAgora= k[: , 0]
# print(eAgora)


# matriz = np.array([
#     [17,22,43],
#     [27,25,14]
#     [15,24,32]
# ])
# print(matriz)
# print(matriz[0][1])
# print(matriz.shape)
# print(matriz.max())
# print(matriz.sum())
# print(matriz.mean())
# print(matriz.std())


#gerar jogo da mega sena

# from datetime import datetime

# # Criando uma semente baseada no tempo (microsegundos)
# seed = datetime.now().microsecond
# gerador = np.random.default_rng(seed)

# # Gerando 6 números únicos entre 1 e 60
# jogo = gerador.choice(np.arange(1, 61), size=6, replace=False)

# # Ordenando os números (como nos resultados oficiais)
# jogo = np.sort(jogo)

# print("Jogo da Mega-Sena:", jogo)


# j = np.array([1,1,2,3,1,3,2,3,6,5,4,3,1])
# j = np.unique(j)
# print(j)


# from datetime import datetime
# gerador = np.random.default_rng(datetime.today().microsecond)
# i= gerador.integers(10, size=(3,4))
# print(i)


# i= gerador.random.random(3)
# print(i)

# h= np.random.random((3,4))
# print(h)

# g - np.random.random((5))
# print(g)
# g2 = np.random.randn((5))
# print(g2)

                     
# g = np.ones(5)
# prit(g)

# f= np.eye(5)
# print(f)

# e = np.ones([1,5])
# print(e)


# d= np.zeros((5,3))
# print (d)


# c = np.empety([3,2], dtype = int)
# print(c)
# print(C.dtype)


# b = np.array([[7,2,23],[12,27,4],[5,34,23]])
# print(b)
# print(b.dtype)

# a3 = np.array ([1.4,3.6,-5.1,9.42])
# print(a3)
# print(a3.dtype)
# a4 = a3.astype(np.int32)
# print(a4)
# print(a4.dtype)
# a5 = np.array([1,2,3,4,])
# print (a5)
# a6 = a5 astype(float)

# a1 = np.array([1,2,3], dtype = np.float64)
# a2 = np.array([1,2,3], dtype = np.int32)
# print(a1)
# print(a1.dtype)
# print(a2)
# print(a2.dtype)



# a = np.array([12,54,3,2,1,7,6])
# print(a)
# print(a.dtype)


