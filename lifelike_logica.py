from random import randint
import pickle

def reinicio_random(filas, columnas):
    return generar_matriz(filas, columnas)

def reinicio_neutro(filas, columnas):
    return [[0 for c in range(columnas)] for f in range(filas)]
    
def generar_matriz(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]    

def obtener_vecinos(M, f, c):
    """Función que retorna una lista con los estados de
    los 8 vecinos de la célula en la posición f, c de M."""
    vecinos = []
    for  filavecinos in range(f-1, f+2):
        for columnavecinos in range(c-1, c+2):
            filavecinos = filavecinos % len(M)
            columnavecinos = columnavecinos % len(M[0])
            if filavecinos != f or columnavecinos != c:
                vecinos.append(M[filavecinos][columnavecinos])
    return vecinos

def transicion_celula(estado, vecinos, nacimiento, supervivencia):

    vivos = vecinos.count(1)

    if estado == 0:
        if vivos in nacimiento:
            return 1
        return 0

    if vivos in supervivencia:
        return 1

    return 0
    

def transicion(M, nacimiento, supervivencia):
    """Toma a la matriz completa y le aplica la función de
    transición a cada célula con su propio vecindario y deja
    el resultado en una matriz nueva."""
    matriz2= []
    for f in range(len(M)):
        fila =[]
        for c in range(len(M[0])):
            vecinos = obtener_vecinos(M, f, c)
            estado2 = transicion_celula(M[f][c], vecinos)
            fila.append(estado2)
        matriz2.append(fila)
    return matriz2

def guardar(nombre, datos):

    archivo = open(nombre, "wb")
    pickle.dump(datos, archivo)
    archivo.close()

def cargar(nombre):

    archivo = open(nombre, "rb")
    datos = pickle.load(archivo)
    archivo.close()

    return datos
