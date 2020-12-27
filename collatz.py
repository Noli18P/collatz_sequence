def collatz(num):
    if (num % 2 == 0):
        num = num / 2
        return num
    else:
        num = num * 3 + 1
        return num 

numero_usuario = input('Ingresa un entero: ')
numero_usuario = int(numero_usuario)

while numero_usuario > 1:
    print(collatz(numero_usuario))
    numero_usuario = collatz(numero_usuario)