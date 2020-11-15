def camino(i, j, matrizCalles):
    row=len(matrizCalles)-1
    col=len(matrizCalles[0])-1

    if i==row and j==col:
        return [[i, j]]
 
    if matrizCalles[i][j] == 1:
        return []
 
    matrizCalles[i][j] = -1
 
    if i > 0 and matrizCalles[i - 1][j] in [0, 1]:                     # Arriba
        recorrido = camino(i - 1, j, matrizCalles)
        if recorrido: 
            return [[i, j]] + recorrido 
 
    if j < len(matrizCalles[i]) - 1 and matrizCalles[i][j + 1] in [0, 1]: # Derecha
        recorrido = camino(i, j + 1, matrizCalles)
        if recorrido: 
            return [[i, j]] + recorrido
 
    if i < len(matrizCalles) - 1 and matrizCalles[i + 1][j] in [0, 1]:    # Abajo
        recorrido = camino(i + 1, j, matrizCalles)
        if recorrido:
            return [[i, j]] + recorrido
 
    if j > 0 and matrizCalles[i][j - 1] in [0, 1]:                     # Izquierda
        recorrido = camino(i, j - 1, matrizCalles) 
        if recorrido: 
            return [[i, j]] + recorrido
 
    return []

def organizar(C, lista):
    rows=len(C)
    col=len(C[0])

    matriz = [0] * rows
    for i in range(rows):
        matriz[i] = [0] * col

    for i in lista:
        matriz[i[0]][i[1]]=1

    return matriz

def encontrar_ruta(C):
    lista= camino(0,0, C)
    if lista ==[]:
        return []
    else:
        return organizar(C, lista)

