import genera_matriz as ma

matriz = ma.cargar_matriz('matriz_aleatoria.txt')
fil = matriz.shape[0]
col = matriz.shape[1]

<<<<<<< HEAD
<<<<<<< HEAD
params = {}  # Se crea el diccionario de parametros
paramsd = {}  # Se crea el diccionario de parametros

for x in range(0, fil):
    for y in range(0, col):
        params[(x, y)] = (('V', False), ('O', False), ('I', False), ('X', False), ('S',False))

params[(0, 5)] = (('V', False), ('O', False), ('I', True), ('X', False), ('S',False))


humano = {0: False, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 5}

def agente():

    for i in range(0, fil):
        for j in range(0, col):
            lista_params = params[(i, j)]
            for param in lista_params:
                if(param[0]=='I'):
                   if(param[1]):
                    print(param)
                    print(i,j)
agente()
=======
params = {}             #Se crea el diccionario de parametros
=======
params = {}  # Se crea el diccionario de parametros
>>>>>>> d61333a120f729b39401d7c516e5a5b8fd2b3e1c

for x in range(0, fil):
    for y in range(0, col):
        params[(x, y)] = (('V', False), ('O', False), ('I', False), ('X', False), ('S',False))

params[(0, 5)] = (('V', False), ('O', False), ('I', True), ('X', False), ('S',False))


humano = {0: False, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 5}#definicion humano

def agente():

<<<<<<< HEAD

    return param
>>>>>>> 57155bb2e424246eaa3e539bacbe1b46597428a4
=======
    for i in range(0, fil):
        for j in range(0, col):
            lista_params = params[(i, j)]
            for param in lista_params:
                if(param[0]=='I'):
                   if(param[1]):
                    print(param)
                    print(i,j)
agente()
>>>>>>> d61333a120f729b39401d7c516e5a5b8fd2b3e1c
