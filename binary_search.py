def binary_search(array, item, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    if begin <= end:
        medium = (begin + end) // 2
        if array[medium] == item:
            return medium  # Retorna a posição do item
        elif item < array[medium]:
            return binary_search(array, item, begin, medium - 1)  # Left (Recursion)
        else:
            return binary_search(array, item, medium + 1, end)  # Right (Recursion)
    return None  # Item não encontrado

array = [0, 1, 2, 3, 4, 5, 6, 42, 8, 9]
item = 42

posicao = binary_search(array, item)
print("Posição do item:", posicao)  # Saída: Posição do item: 6

#Complexidade = O (log n)
#Precisa estar ordenado
