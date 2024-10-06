# Importe de modulos necesarios
from modules.menu import ejecutar_opcion, pedir_lista, pedir_numero

# Ingreso de valores
list = pedir_lista('Ingrese los valores númericos de la lista separado por espacios: ')
while True: # Bucle
    try:
        option = pedir_numero('Opciones:\n 1. Ordenamiento Burbuja (Bubble Sort)\n 2. Ordenamiento por Selección (Selection Sort)\n 3. Ordenamiento por Inserción (Insertion Sort)\n 4. Ordenamiento Rápido (Quick Sort)\n 5. Salir\nIngrese una opción: ')
        ejecutar_opcion(list,option) 

    except ValueError: # Manejo de errores
        print('\nError: Ingreso de valor no numerico.')