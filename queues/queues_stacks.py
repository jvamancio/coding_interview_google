"""
Uma fila (queue) é uma estrutura de dados linear que segue a política FIFO (First In, First Out), 
o que significa que o primeiro elemento inserido é o primeiro a ser removido. 
Isso é análogo a uma fila de pessoas em um banco: a primeira pessoa que entra na fila é a primeira a 
ser atendida (removida da fila).

Operações Básicas em Filas:
Enqueue: Adiciona um item ao final da fila.
Dequeue: Remove o item do início da fila.
Front/Peek: Retorna o item no início da fila sem removê-lo.
isEmpty: Verifica se a fila está vazia
"""

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

# Exemplo
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(3)
print(queue.dequeue())  # Saída: 1
print(queue.dequeue())  # Saída: 2
print(queue.dequeue())  # Saída: 2
print(queue.dequeue())  # Saída: 2
