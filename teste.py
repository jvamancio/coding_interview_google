#árvore binária de busca ordenada (BTS) Característica: Garantem tempo O(log n) para operações de busca, inserção e exclusão:
#Classe: Agrupa dados e métodos relacionados em uma estrutura única, oferecendo organização, reutilização, abstração e facilidade de expansão.
#Uso no Exemplo: A classe Node encapsula a estrutura de um nó de uma árvore binária, tornando o código mais limpo e modular, além de facilitar a implementação de operações na árvore.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#função para inserir na árvore binária de busca ordenada (BTS): 
def insert_bst(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert_bst(root.left, data)
        else:
            root.right = insert_bst(root.right, data)
    return root

#função para construir a árvore binária de busca ordenada (BTS): 
def build_bst_from_array(arr):
    root = None
    for data in arr:
        root = insert_bst(root, data)
    return root

def findMaxUtil(root):
    if root is None:
        return 0

    l = findMaxUtil(root.left)
    r = findMaxUtil(root.right)

    max_single = max(max(l, r) + root.data, root.data)

    max_top = max(max_single, l + r + root.data)

    findMaxUtil.res = max(findMaxUtil.res, max_top)

    return max_single

def findMaxSum(root):
    findMaxUtil.res = float("-inf") #float("-inf") representa o menor valor possível em ponto flutuante. Em outras palavras, é uma representação do conceito de "menos infinito".
    findMaxUtil(root)
    return findMaxUtil.res

# Driver code
if __name__ == '__main__':
    arr = [10, 2, 11, 20, 1, -25, 3, 4]
    root = build_bst_from_array(arr)
    print("Max path sum is", findMaxSum(root))