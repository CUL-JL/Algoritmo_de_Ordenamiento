def selection_sort(list):
    original_list = list.copy() # Copia de la lista original
    iteraciones = 0   # Contador de iteraciones
    for i in range(len(list)): # Ciclo para recorrer la lista
        iteraciones += 1 
        min_index = i # Indice del elemento minimo

        for j in range(i + 1, len(list)): # Ciclo para comparar los elementos de la lista
            if list[j] < list[min_index]: # Si el elemento actual es menor al minimo
                min_index = j # Asignar el indice del elemento actual

        list[i], list[min_index] = list[min_index], list[i] # Intercambiar los elementos

    # Retorna una impresion de la lista original, la lista ordenada y el numero de iteraciones que tomo ordenar la lista
    return print(f'Lista original: {original_list}\nLista ordenada: {list}\nNumero de iteraciones: {iteraciones}\n')