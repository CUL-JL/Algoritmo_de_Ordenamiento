def bubble_sort(list):
    original_list = list.copy()  # Copia de la lista original
    iteraciones = 0  # Contador de iteraciones
    for i in range(len(list) - 1):
        iteraciones += 1  
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    
    return print(f'Lista original: {original_list}\nLista ordenada: {list}\nNumero de iteraciones: {i + 1}\n')