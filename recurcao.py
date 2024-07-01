#função para calcular o fatorial de um número de forma recursiva
#A função recursiva chama ela mesma dentro da própria função até chegar no caso base 
def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1) 
    
x = int(input("digite um numero para calcular seu fatorial: "))
res = fatorial(x)
print("O fatorial de %d é %d " % (x,res))