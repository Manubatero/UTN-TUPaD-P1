# Ejercicio N° 1

# Funcion recursiva
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitamos al usuario que ingrese un numero entero
num = int(input("Introduce un número entero: "))

# Validamos que el numero sea mayor o igual a 1
if num < 1:
    print("Por favor, introduce un número entero mayor o igual a 1.")
else:
    # Calcula y muestra el factorial de cada numero entre 1 y el número ingresado
    for i in range(1, num + 1):
        print(f"Factorial de {i} es: {factorial(i)}")

# Ejercicio N° 2

# Funcion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario la cantidad de terminos que desea ver en la serie
num = int(input("Introduce un numero entero para la serie Fibonacci: "))

# Validacion para asegurarnos de que sea un numero positivo
if num < 0:
    print("Por favor, introduce un número entero positivo.")
else:
    print(f"Serie de Fibonacci hasta la posicion {num}:")
    for i in range(num + 1):
        print(fibonacci(i), end=" ")

# Ejercicio N° 3

# Funcion
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Solicitar al usuario la base y el exponente
base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

# Calculo y muestra el resultado
resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

# Ejercicio N° 4

# Funcion
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)  # Llamada recursiva con n//2 y concatenacion del resto

# Solicitar al usuario un numero entero positivo
num = int(input("Introduce un numero entero positivo: "))

# Validar que el numero sea positivo
if num < 0:
    print("Por favor, introduce un numero positivo.")
else:
    resultado = decimal_a_binario(num)
    print(f"El numero {num} en binario es: {resultado}")

# Ejercicio N° 5 

# Funcion
def es_palindromo(palabra):
    if len(palabra) <= 1:  # Si la palabra tiene 0 o 1 caracteres, es palindromo
        return True
    elif palabra[0] != palabra[-1]:  # Si el primer y ultimo caracter no coinciden, no es palindromo
        return False
    else:
        return es_palindromo(palabra[1:-1])  # Llamada recursiva con la palabra sin los extremos

# Pruebas con diferentes palabras
palabras = ["reconocer", "radar", "python", "neuquen", "anilina"]
for palabra in palabras:
    print(f"{palabra}: {es_palindromo(palabra)}")

# Ejercicio N° 6

# Funcion 
def suma_digitos(n):
    if n < 10:  # Caso base: si n tiene un solo digito, retorna n
        return n
    else:  # Caso recursivo: suma el ultimo digito y llama con el numero sin el ultimo digito
        return (n % 10) + suma_digitos(n // 10)

# Pruebas con ejemplos de la consigna
print(suma_digitos(1234))  # 10 (1 + 2 + 3 + 4)
print(suma_digitos(9))     # 9
print(suma_digitos(305))   # 8 (3 + 0 + 5)

# Ejercicio N° 7

# Funcion
def contar_bloques(n):
    if n == 1:
        return 1  # Caso base: una piramide de un solo nivel tiene un solo bloque
    else:
        return n + contar_bloques(n - 1)  # Caso recursivo: suma los bloques del nivel actual con los del nivel anterior

# Pruebas con los ejemplos de la consigna
print(contar_bloques(1))  # 1 (solo el primer nivel)
print(contar_bloques(2))  # 3 (2 + 1)
print(contar_bloques(4))  # 10 (4 + 3 + 2 + 1)

# Ejercicio N° 8

# funcion 
def suma_digitos(n):
    if n < 10:  # Caso base: si n tiene un solo digito, retorna n
        return n
    else:  # Caso recursivo: suma el ultimo digito y llama con el numero sin el ultimo digito
        return (n % 10) + suma_digitos(n // 10)

# Pruebas con ejemplos de la consigna
print(suma_digitos(1234))  # 10 (1 + 2 + 3 + 4)
print(suma_digitos(9))     # 9
print(suma_digitos(305))   # 8 (3 + 0 + 5)