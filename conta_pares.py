def count_pairs(nums, target):
    """
    Conta o número de pares únicos de inteiros em uma lista que somam um valor alvo.

    Args:
        nums (list[int]): A lista de números inteiros positivos.
        target (int): A soma alvo.

    Retorna:
        int: O número de pares únicos com a soma alvo.
    """

    num_counts = {}  # Tabela hash para armazenar contagens de números
    unique_pairs = 0  # Contador para pares únicos
    unique_pairs_list = []  # List to store unique pairs
    for num in nums:
        complement = target - num  # Calcula o complemento
        print(complement)
        # Verifica se o complemento existe na tabela hash
        if complement in num_counts:
            unique_pairs += num_counts[complement]  # Aumenta a contagem de pares únicos
            unique_pairs_list.append((num, complement))  # Add pair to list
            # Incrementa a contagem do número atual
            num_counts[complement] += 1
        else:
            # Adiciona o número atual à tabela hash com contagem 1
            num_counts[num] = 1
    
    print("Pares únicos com soma igual a", target, ":", unique_pairs_list)

    return unique_pairs

nums = [6, 3, 7, 12, 1, 2, 0, 11]
target = 9

unique_pairs_count = count_pairs(nums, target)
print("Número de pares únicos com soma:",target,"é ", unique_pairs_count)  # Saída: 3
