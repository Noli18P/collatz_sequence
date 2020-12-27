def collatz(numero):
    if numero % 2 == 0:
        return numero / 2
    if numero & 2 == 1:
        return numero * 3 + 1

def main():
    numeroUsuario = int(input('Ingresa un numero entero: '))
    terminar = 0
    
    while terminar != 1:
        collatz(collatz(numeroUsuario))

        
    
main()