def selection_sort(list):
    original_list = list.copy()  
    iteraciones = 0  
    for i in range(len(list)):
        iteraciones += 1
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]

    return print(f'Lista original: {original_list}\nLista ordenada: {list}\nNumero de iteraciones: {iteraciones}\n')