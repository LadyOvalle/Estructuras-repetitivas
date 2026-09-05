'''Pirámide de asteriscos:
Dibuja una pirámide de altura n.'''

n = int(input("Ingrese la altura de la pirámide: "))

for i in range(1, n + 1):
    print("*" * i)