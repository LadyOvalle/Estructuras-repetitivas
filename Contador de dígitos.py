'''Contador de dígitos:
Cuenta cuántos dígitos tiene un número entero.'''

n = int(input("Ingrese un número entero: "))
num = abs(n)
contador = 0

if num == 0:
    contador = 1

else:
    while num > 0:
        num //= 10
        contador += 1
        print("El número tiene", contador, "dígitos.")