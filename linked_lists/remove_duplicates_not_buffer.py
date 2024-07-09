"""
Solução Sem Utilizar Buffer Temporário
Se não podemos utilizar um buffer temporário como um conjunto, 
podemos resolver o problema com uma abordagem de tempo O(n^2), 
onde n é o número de elementos na lista ligada. Para cada nó na lista, 
verificamos todos os nós subsequentes para ver se há duplicatas e, 
se houver, removemos o nó.
"""
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_duplicates_no_buffer(head):
    current = head
    
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    
    return head

# Exemplo de uso
# Continuando com a lista ligada original do exemplo anterior: 3 -> 1 -> 3 -> 5 -> 1 -> 7

# Exemplo de uso
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

head = ListNode(3)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(7)

print("Lista ligada original:")
print_linked_list(head)

head = remove_duplicates_no_buffer(head)

print("Lista ligada após remover duplicatas sem buffer:")
print_linked_list(head)
