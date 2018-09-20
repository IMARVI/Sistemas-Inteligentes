import functools

#  Creamos nuestra clase nodo
class Nodo:
    def __init__(self, estado, padre, accion, profundidad):
        self.estado = estado
        self.padre = padre
        self.accion = accion
        self.profundidad = profundidad
        self.heuristica = -1

#  Expandimos los nodos y verificamos si se encuentra en alguna frontera
#  Si se encuentra en frontera, limitamos los hijos a expandir
def hijo(estado, move_dir):
    temp = estado[:]

    i = temp.index(0)

    if move_dir == 'L':
        if i not in [0, 3, 6]:
            temp[i - 1], temp[i] = temp[i], temp[i - 1]
            return temp
        else:
            return None
    elif move_dir == 'R':
        if i not in [2, 5, 8]:
            temp[i + 1], temp[i] = temp[i], temp[i + 1]
            return temp
        else:
            return None
    elif move_dir == 'U':
        if i not in [0, 1, 2]:
            temp[i - 3], temp[i] = temp[i], temp[i - 3]
            return temp
        else:
            return None
    elif move_dir == 'D':
        if i not in [6, 7, 8]:
            temp[i + 3], temp[i] = temp[i], temp[i + 3]
            return temp
        else:
            return None

#  Metodo en el cual se insertan los hijos del nodo actual
def expandir(nodo):
    hijos = [
        Nodo(hijo(nodo.estado, 'U'), nodo, 'U', nodo.profundidad + 1),
        Nodo(hijo(nodo.estado, 'D'), nodo, 'D', nodo.profundidad + 1),
        Nodo(hijo(nodo.estado, 'L'), nodo, 'L', nodo.profundidad + 1),
        Nodo(hijo(nodo.estado, 'R'), nodo, 'R', nodo.profundidad + 1)
    ]

    #  Limpiamos el arreglo de los posibles 'None'
    hijos = [nodo for nodo in hijos if nodo.estado is not None]
    return hijos


def a_star(initial, final, heuristica):
    #  Comenzamos con nuestro nodo Raiz
    nodes = [Nodo(initial, None, None, 0)]
    iteraciones = 0

    while nodes:
        for nodo in nodes:
            #  Calculamos la heuristicaa de nuestro estado actual
            nodo.heuristica = nodo.profundidad + heuristica(nodo.estado, final)
            #  Iteramos nuestra lista de nodos y verificamos cual tiene la menor heuristicaa
            #  El nodo con menor heuristicaa es el que asignamos a nuestro valor nodo
            nodo = functools.reduce(lambda smallest, current: smallest if (smallest.heuristica <= current.heuristica) else current, nodes)

        #  Validamos que nuestro nodo seleccionado sea el final
        if nodo.estado == final:
            moves = []
            temp = nodo
            
            while 1:
                #  Insertamos los movimientos para llegar al estado final
                moves.insert(0, temp.accion)
                #  Rompemos al llegar al nodo siguiente de la Raiz
                if temp.profundidad == 1:
                    break
                #  Cambiamos de nodo al nodo padre para sacar su valor en al prox iteracion
                temp = temp.padre
            return moves

        #  En el caso de no ser el nodo final, expandimos el nodo
        nodes = expandir(nodo)
        iteraciones += 1

        #  Evitamos un desbordamiento de memoria limitando a 200_000 iteraciones
        if iteraciones == 200000:
            return []
    return []

#  Sacamos la distancia Manhattan
def manhattan(estado, final):
    distancia = 0
    #  buscamos la fila y la columna del estado y sacamos la distancia de cada punto.
    for i in range(len(estado)):
        if estado[i] != 0:
            fila = int(final.index(estado[i]) / 3)
            columna = final.index(estado[i]) % 3
            distancia += abs(fila - int(i / 3)) + abs(columna - (i % 3))
    return distancia

#  heuristicaa que calcula la diferencia tomando la posicion de cada numero
def fuera_lugar(estado, final):
    distancia = 0

    for i in range(len(estado)):
        if estado[i] != final[i] and estado[i] != 0:
            distancia += 1
        i += 1
    return distancia


#  1 = Manhattan  0 = Cuadros fuera de lugar
def busquedaAstar(edoInicial, edoFinal, heuristica):

    inicial_list = [num for elem in edoInicial for num in elem]
    objetivo_list = [num for elem in edoFinal for num in elem]

    if heuristica == 0:
        return a_star(inicial_list, objetivo_list, fuera_lugar)
    elif heuristica == 1:
        return a_star(inicial_list, objetivo_list, manhattan)
    else:
        return []
