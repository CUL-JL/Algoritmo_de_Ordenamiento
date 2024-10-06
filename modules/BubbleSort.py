def bubble_sort(list):
    iteraciones = 0  # Contador de iteraciones
    original_list = list.copy()  # Copia de la lista original

    for i in range(len(list) - 1): # Ciclo para recorrer la lista
        iteraciones += 1  

        for j in range(len(list) - 1 - i): # Ciclo para comparar los elementos de la lista
            if list[j] > list[j + 1]: # Si el elemento actual es mayor al siguiente
                list[j], list[j + 1] = list[j + 1], list[j] # Intercambiar los elementos

    # Retorna una impresion de la lista original, la lista ordenada y el numero de iteraciones que tomo ordenar la lista
    return print(f'Lista original: {original_list}\nLista ordenada: {list}\nNumero de iteraciones: {i + 1}\n')