def insertion_sort(list):
    iteraciones = 0  # Contador de iteraciones
    original_list = list.copy() # Copia de la lista original
    for i in range(1, len(list)): # Ciclo para recorrer la lista
        iteraciones += 1  
        key = list[i]  # Elemento actual
        j = i - 1 # Indice del elemento anterior al actual
        
        while j >= 0 and list[j] > key: # Mientras el indice sea mayor o igual a 0 y el elemento anterior sea mayor al actual
            list[j + 1] = list[j]  # Intercambiar los elementos
            j -= 1 # Decrementar el indice

        list[j + 1] = key  # Asignar el elemento actual en la posicion correcta

    # Retorna una impresion de la lista original, la lista ordenada y el numero de iteraciones que tomo ordenar la lista
    return print(f'Lista original: {original_list}\nLista ordenada: {list}\nNumero de iteraciones: {iteraciones}\n')