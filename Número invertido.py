'''Número invertido:
Invierte los dígitos de un número entero.'''

n = int(input("Ingrese su número entero: "))

numero = abs(n)
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

if n < 0:
    invertido = -invertido

print("Número invertido: ", invertido)