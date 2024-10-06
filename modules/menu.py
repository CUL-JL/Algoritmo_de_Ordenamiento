# Iporte de modulos 
from modules.BubbleSort import bubble_sort
from modules.SelectionSort import selection_sort
from modules.InsertionSort import insertion_sort
from modules.QuickSort import quick_sort

# Funciones secundarias
def pedir_numero(num):
    while True: # Bucle
        try: return int(input(num)) # Retorno de valor numérico
        except ValueError: print('Error: ingreso de valor no numérico.\n') # Manejo de errores

def pedir_cadena(txt):
    while True: # Bucle
        try: return input(txt) # Retorno de valor numérico
        except ValueError: print('Error: ingreso de valor no valido.\n') # Manejo de errores

def pedir_lista(txt):
    while True: # Bucle
        try: return list(map(int, input(txt).split())) # Retorno de valor numérico
        except ValueError: print('Error: ingreso de valor no numérico.\n') # Manejo de errores

# Funciones principales
def ejecutar_opcion(list, option):
    list_copy = list.copy() # Copia de la lista original
    match option:
        case 1: # Ordenamiento Burbuja (Bubble Sort)
            bubble_sort(list_copy) # Llamado a la función de ordenamiento Burbuja
        
        case 2: # Ordenamiento por Selección (Selection Sort)
            selection_sort(list_copy) # Llamado a la función de ordenamiento por Selección

        case 3: # Ordenamiento por Inserción (Insertion Sort)
            insertion_sort(list_copy) # Llamado a la función de ordenamiento por Inserción

        case 4: # Ordenamiento Rápido (Quick Sort)
            quick_sort(list_copy) # Llamado a la función de ordenamiento Rápido

        case 5: print('Saliendo del programa...'); exit() # Salir del programa

        case _: print('Error: Opción no valida.\n') # Manejo de errores