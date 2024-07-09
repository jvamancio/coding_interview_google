class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_duplicates(head):
    if not head:
        return head
    
    seen = set()
    current = head
    seen.add(current.value)
    
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next
            
    return head

# Exemplo de uso
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Criando uma lista ligada de exemplo: 3 -> 1 -> 3 -> 5 -> 1 -> 7
head = ListNode(3)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next = ListNode(7)

print("Lista ligada original:")
print_linked_list(head)

head = remove_duplicates(head)

print("Lista ligada após remover duplicatas:")
print_linked_list(head)
