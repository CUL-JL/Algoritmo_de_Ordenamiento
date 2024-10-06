def insertion_sort(list):
    iteraciones = 0  
    original_list = list.copy()
    for i in range(1, len(list)):
        iteraciones += 1  
        key = list[i]  
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]  
            j -= 1
        
        list[j + 1] = key  
    
    return print(f'Lista original: {original_list}\nLista ordenada: {list}\nNumero de iteraciones: {iteraciones}\n')