import nodo
from copy import deepcopy

#  variable la cual contiene la matriz objetivo
estadoFinal = []

#  Listas que nos ayudaran a guardar las string y los estados de cada hoja creada
filaNodo = []
filaMove = []

#  Lista que nos ayudara a buscar los estados que ya hemos encontrado 
nodosVisitados = []

#  n es el nodo que vamos a validar su estado con el estado fina, regresa un True o False dependiendo la igualación
def comprobar(n):
    if n.estado == estadoFinal:
        print(n.accion)
        return True
    else:
        return False

#  n es el nodo que evaluaremos los posibles movimientos que puede tener el espacion en blanco
#  Una vez identificado los movimientos, metemos la letra y la nueva matriz en sus respectivas listas y las regresamos en una lista de listas
def hijosPosibles(n):

    hijos = []
    hojas = []

    #  si el 0 se encuetra en la primera fila
    if 0 in n.estado[0]:
        index = n.estado[0].index(0)
        if index == 0:
            hijos.append("R")
            temporal = deepcopy(n.estado)
            temporal[0][0] = n.estado[0][1]
            temporal[0][1] = 0
            hojas.append(temporal)

            hijos.append("D")
            temporal = deepcopy(n.estado)
            temporal[0][0] = n.estado[1][0]
            temporal[1][0] = 0
            hojas.append(temporal)

        elif index == 1:
            hijos.append("R")
            temporal = deepcopy(n.estado)
            temporal[0][1] = n.estado[0][2]
            temporal[0][2] = 0
            hojas.append(temporal)

            hijos.append("D")
            temporal = deepcopy(n.estado)
            temporal[0][1] = n.estado[1][1]
            temporal[1][1] = 0
            hojas.append(temporal)

            hijos.append("L")
            temporal = deepcopy(n.estado)
            temporal[0][1] = n.estado[0][0]
            temporal[0][0] = 0
            hojas.append(temporal)

        elif index == 2:
            hijos.append("D")
            temporal = deepcopy(n.estado)
            temporal[0][2] = n.estado[1][2]
            temporal[1][2] = 0
            hojas.append(temporal)

            hijos.append("L")
            temporal = deepcopy(n.estado)
            temporal[0][2] = n.estado[0][1]
            temporal[0][1] = 0
            hojas.append(temporal)
    
    #  Si el 0 se encuentra en la segunda fila
    elif 0 in n.estado[1]:
        index = n.estado[1].index(0)
        if index == 0:
            hijos.append("D")
            temporal = deepcopy(n.estado)
            temporal[1][0] = n.estado[2][0]
            temporal[2][0] = 0
            hojas.append(temporal)

            hijos.append("R")
            temporal = deepcopy(n.estado)
            temporal[1][0] = n.estado[1][1]
            temporal[1][1] = 0
            hojas.append(temporal)

            hijos.append("U")
            temporal = deepcopy(n.estado)
            temporal[1][0] = n.estado[0][0]
            temporal[0][0] = 0
            hojas.append(temporal)

        elif index == 1:
            hijos.append("D")
            temporal = deepcopy(n.estado)
            temporal[1][1] = n.estado[2][1]
            temporal[2][1] = 0
            hojas.append(temporal)

            hijos.append("L")
            temporal = deepcopy(n.estado)
            temporal[1][1] = n.estado[1][0]
            temporal[1][0] = 0
            hojas.append(temporal)

            hijos.append("R")
            temporal = deepcopy(n.estado)
            temporal[1][1] = n.estado[1][2]
            temporal[1][2] = 0
            hojas.append(temporal)

            hijos.append("U")
            temporal = deepcopy(n.estado)
            temporal[1][1] = n.estado[0][1]
            temporal[0][1] = 0
            hojas.append(temporal)

        elif index == 2:
            hijos.append("D")
            temporal = deepcopy(n.estado)
            temporal[1][2] = n.estado[2][2]
            temporal[2][2] = 0
            hojas.append(temporal)

            hijos.append("L")
            temporal = deepcopy(n.estado)
            temporal[1][2] = n.estado[1][1]
            temporal[1][1] = 0
            hojas.append(temporal)

            hijos.append("U")
            temporal = deepcopy(n.estado)
            temporal[1][2] = n.estado[0][2]
            temporal[0][2] = 0
            hojas.append(temporal)
    
    #  Si el 0 se encuentra en la tercera fila
    else:
        index = n.estado[2].index(0)
        if index == 0:
            hijos.append("U")
            temporal = deepcopy(n.estado)
            temporal[2][0] = n.estado[1][0]
            temporal[1][0] = 0
            hojas.append(temporal)

            hijos.append("R")
            temporal = deepcopy(n.estado)
            temporal[2][0] = n.estado[2][1]
            temporal[2][1] = 0
            hojas.append(temporal)

        elif index == 1:
            hijos.append("U")
            temporal = deepcopy(n.estado)
            temporal[2][1] = n.estado[1][1]
            temporal[1][1] = 0
            hojas.append(temporal)

            hijos.append("L")
            temporal = deepcopy(n.estado)
            temporal[2][1] = n.estado[2][0]
            temporal[2][0] = 0
            hojas.append(temporal)

            hijos.append("R")
            temporal = deepcopy(n.estado)
            temporal[2][1] = n.estado[2][2]
            temporal[2][2] = 0
            hojas.append(temporal)

        elif index == 2:
            hijos.append("U")
            temporal = deepcopy(n.estado)
            temporal[2][2] = n.estado[1][2]
            temporal[1][2] = 0
            hojas.append(temporal)

            hijos.append("L")
            temporal = deepcopy(n.estado)
            temporal[2][2] = n.estado[2][1]
            temporal[2][1] = 0
            hojas.append(temporal)

    x = [hijos, hojas]
    return x

#  este metodo recibe una lista de listas y un nodo padre
#  creamos nuevos nodos dependiendo de la cantidad de posibles hijos del padre y los metemos a la lista filaNodo
def expandir1(lista,padre):

    while lista[0].__len__() > 0:
        accion = deepcopy(padre.accion)
        accion.append(lista[0].pop(0))
        n = nodo.Nodo(lista[1].pop(0),padre,accion,padre.costo+1)
        filaNodo.append(n)


def busquedaNoInformada(edoInicial, edoFinal, algoritmo):
    global estadoFinal

    estadoFinal = edoFinal
    n = nodo.Nodo(edoInicial, None, [], 1)
    _busquedaNoInformada(n, algoritmo)


def _busquedaNoInformada(n, a):

    if comprobar(n):
        return n.accion
    else:
        #  Revisamos el tipo de algoritmo que ocuparemos 0 = BSF, 1 = DSF
        if a == 0:
                mov = hijosPosibles(n)
                nodosVisitados.append(n.estado)
                expandir1(mov, n)

                if filaNodo == 0:
                    print("NO hay solucion")
                    return 
                _busquedaNoInformada(filaNodo.pop(0), 0)
            

        elif a == 1:            
            if n.estado in nodosVisitados:
                _busquedaNoInformada(filaNodo.pop(), 1)
            else:
                mov = hijosPosibles(n)
                nodosVisitados.append(n.estado)
                expandir1(mov, n)

                if filaNodo == 0:
                    print("NO hay solucion")
                    return 
                _busquedaNoInformada(filaNodo.pop(), 1)
