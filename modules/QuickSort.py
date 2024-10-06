def ordenar_rapido(lista, inicio, fin, contador):
    if inicio < fin: # Si el inicio es menor al fin
        pivote_indice = particionar(lista, inicio, fin, contador) # Particionar la lista
        ordenar_rapido(lista, inicio, pivote_indice - 1, contador) # Ordenar la lista
        ordenar_rapido(lista, pivote_indice + 1, fin, contador) # Ordenar la lista

    return lista # Retorna la lista ordenada

def particionar(lista, inicio, fin, contador):
    pivote = lista[fin] # Pivote es el ultimo elemento de la
    i = inicio - 1 # Indice del elemento anterior al inicio
    for j in range(inicio, fin): # Ciclo para recorrer la lista
        contador[0] += 1  # Incrementar el contador
        if lista[j] <= pivote: # Si el elemento actual es menor o igual al pivote
            i += 1 # Incrementar el indice
            lista[i], lista[j] = lista[j], lista[i] # Intercambiar los elementos
            
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1] # Intercambiar los elementos
    return i + 1 # Retorna el indice del pivote

def quick_sort(lista):
    contador = [0] # Contador de iteraciones
    original_list = lista.copy() # Copia de la lista original
    ordenar_rapido(lista, 0, len(lista) - 1, contador) # Ordenar la lista

    # Retorna una impresion de la lista original, la lista ordenada y el numero de iteraciones que tomo ordenar la lista
    return print(f'Lita original: {original_list}\nLista ordenada: {lista}\nNumero de iteraciones: {contador[0]}\n')