'''FizzBuzz: pide un número n e imprime los números del 1 al n, pero:
Si el número es múltiplo de 3, imprime "Fizz".
Si el número es múltiplo de 5, imprime "Buzz".
Si es múltiplo de ambos, imprime "FizzBuzz".'''

n = int(input("Ingresa un número: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)