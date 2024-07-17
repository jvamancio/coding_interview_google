def verificar_grupo(k, array):
    # Contar ocorrências de cada caractere
    contagem = {}
    for char in array:
        if char in contagem:
            contagem[char] += 1
        else:
            contagem[char] = 1
    
    # Verificar quais caracteres pertencem ao grupo
    pertencem = []
    nao_pertencem = []
    vistos = {}  # Para rastrear quais caracteres já processamos

    for char in array:
        if char not in vistos:
            vistos[char] = True
            if contagem[char] >= k:
                pertencem.append(char)
            else:
                nao_pertencem.append(char)
    
    return pertencem, nao_pertencem

# Exemplo de uso
k = 3
array = "AAACCCB"
pertencem, nao_pertencem = verificar_grupo(k, array)

print("Pertencem ao grupo:", pertencem)
print("Não pertencem ao grupo:", nao_pertencem)
