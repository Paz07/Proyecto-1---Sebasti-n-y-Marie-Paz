from random import randint
import pickle

def generar_matriz_vacia(filas, columnas):
    """
    Función que genera una matriz vacía.
    Entradas y restricciones:
    - filas: entero positivo.
    - columnas: entero positivo.
    Salidas:
    Una matriz de ceros de tamaño filas x columnas.
    """
    return [[0 for c in range(columnas)] for f in range(filas)]
    
def generar_matriz_aleatoria(filas, columnas):
    """
    Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1
    Entradas y restricciones:
    - filas: entero positivo.
    - columnas: entero positivo.
    Salidas:
    Una matriz con valores aleatorios de 0 o 1.
    """
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]    

def obtener_vecinos(M, f, c):
    """
    Función que retorna una lista con los estados de
    los 8 vecinos de la célula en la posición f, c de M.
    Entradas y restricciones:
    - M: matriz no vacía.
    - f: fila válida de la matriz.
    - c: columna válida de la matriz.
    Salidas:
    Lista con los estados de las ocho células vecinas.
    """
    vecinos = []
    for  filavecinos in range(f-1, f+2):
        for columnavecinos in range(c-1, c+2):
            filavecinos = filavecinos % len(M)
            columnavecinos = columnavecinos % len(M[0])
            if filavecinos != f or columnavecinos != c:
                vecinos.append(M[filavecinos][columnavecinos])
    return vecinos

def transicion_celula(estado, vecinos, nacimiento, supervivencia):
    """
    Función que calcula el siguiente estado de una célula.
    Entradas y restricciones:
    - estado: 0 o 1.
    - vecinos: lista con estados vecinos.
    - nacimiento: lista de enteros entre 0 y 8.
    - supervivencia: lista de enteros entre 0 y 8.
    Salidas:
    El nuevo estado de la célula.
    """
    vivos = vecinos.count(1)

    if estado == 0:
        if vivos in nacimiento:
            return 1
        return 0

    if vivos in supervivencia:
        return 1

    return 0
    

def transicion(M, nacimiento, supervivencia):
    """
    Toma a la matriz completa y le aplica la función de
    transición a cada célula con su propio vecindario y deja
    el resultado en una matriz nueva.
    Entradas y restricciones:
    - M: matriz no vacía.
    - nacimiento: lista de enteros entre 0 y 8.
    - supervivencia: lista de enteros entre 0 y 8.
    Salidas:
    Una nueva matriz con los estados actualizados.
    """
    matriz2= []
    for f in range(len(M)):
        fila =[]
        for c in range(len(M[0])):
            vecinos = obtener_vecinos(M, f, c)
            estado2 = transicion_celula(M[f][c], vecinos, nacimiento, supervivencia)
            fila.append(estado2)
        matriz2.append(fila)
    return matriz2

def guardar(nombre, datos):
    """
    Función que guarda datos en un archivo.
    Entradas y restricciones:
    - nombre: cadena válida.
    - datos: estructura serializable.
    Salidas:
    Guarda los datos en disco.
    """
    archivo = open(nombre, "wb")
    pickle.dump(datos, archivo)
    archivo.close()

def cargar(nombre):
    """
    Función que carga datos desde un archivo.
    Entradas y restricciones:
    - nombre: cadena válida.
    Salidas:
    Los datos almacenados en el archivo.
    """
    archivo = open(nombre, "rb")
    datos = pickle.load(archivo)
    archivo.close()

    return datos
