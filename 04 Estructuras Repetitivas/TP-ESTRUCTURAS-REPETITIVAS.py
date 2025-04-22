# Ejecicio Nro 1

num = 0 # Definicion de variable con su valor
while num <= 100: # Iniciañizacion del blucle while
    print("Los Numeros enteros del 0 al 100 son:", num) # Se imprime resultado por pantalla
    num += 1 # Contador

# Ejercicio Nro 2 

numero = int(input("Por favor, ingrese la cifra: ")) # Declaracion de Variable Y solicitud de datos al usuario
cantidad_de_digitos = len(str(numero)) # Declaracion de otra variable para almacenar el nro de digito mediante la funcion len()
print(f"El numero tiene {cantidad_de_digitos} digitos") # Se imprime el resultado por pantalla

# Ejercicio Nro 3

num_menor = int(input("Por favor, ingrese el numero menor: ")) # Solicitar al usuario el ingreso del numero menor
num_mayor = int(input("Por favor, ingrese el numero mayor: ")) # Solicitar al usuario el ingreso del numero mayor
if num_menor > num_mayor:
    num_menor, num_mayor = num_mayor, num_menor # Se establece la igualdad de valores, por si el usuario ingresa mal el orden de valores
suma = sum(range(num_menor + 1, num_mayor)) # Operacion aritmetica
print(f"La suma de los numeros entre {num_menor} y {num_mayor} es: {suma}") # se imprime resultado por pantalla

# Ejercicio Nro 4

def sumar_numeros():  # Definimos una función llamada sumar_numeros
    total = 0  # Inicializamos la variable total en 0 para acumular la suma de los números
    numero = int(input("Ingresa un número entero (ingresa 0 para detenerte): "))  # Pedimos al usuario un número y lo convertimos a entero
    
    while numero != 0:  # Mientras el número ingresado no sea 0, seguimos sumando
        total += numero  # Sumamos el número ingresado al total acumulado
        numero = int(input("Ingresa otro número entero (ingresa 0 para detenerte): "))  # Pedimos otro número al usuario
    
    print(f"El total acumulado es: {total}")  # Mostramos el total acumulado al usuario

sumar_numeros()  # Llamamos a la función para que se ejecute

# Ejercicio Nro 5

import random  # Importamos el módulo random para generar un número aleatorio

def juego_adivinanza():  # Definimos la función del juego
    numero_secreto = random.randint(0, 9)  # Generamos un número aleatorio entre 0 y 9
    intentos = 0  # Inicializamos el contador de intentos
    adivinanza = -1  # Inicializamos la variable con un valor diferente al número secreto para entrar en el bucle

    print("¡Bienvenido al juego de adivinanza!")  # Mensaje de bienvenida
    print("Intenta adivinar el número secreto entre 0 y 9.")  # Explicación del juego

    while adivinanza != numero_secreto:  # El bucle continúa hasta que el usuario acierte
        try:
            adivinanza = int(input("Ingresa tu número: "))  # Pedimos al usuario un número y lo convertimos a entero
            intentos += 1  # Incrementamos el contador de intentos

            if adivinanza < 0 or adivinanza > 9:  # Verificamos si el número está dentro del rango permitido
                print("Por favor, ingresa un número válido entre 0 y 9.")
                intentos -= 1  # No contamos intentos inválidos
            
            elif adivinanza != numero_secreto:  # Si el número no es el correcto, le damos otra oportunidad
                print("Incorrecto, intenta nuevamente.")

        except ValueError:  # Capturamos el error si el usuario ingresa algo que no es un número
            print("Entrada inválida. Por favor, ingresa un número entero.")

    print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")  # Mensaje final

juego_adivinanza()  # Llamamos a la función para iniciar el juego

# Ejercicio Nro 6

# Recorremos los números pares desde 100 hasta 0 en orden descendente
for numero in range(100, -1, -2):  # Comenzamos en 100, terminamos en 0, avanzamos de -2 en -2
    print(numero)

# Ejercicio Nro 7

# Pedimos al usuario un número entero positivo
numero = int(input("Ingresa un número entero positivo: "))

# Verificamos que el número ingresado sea positivo
if numero < 0:
    print("Por favor, ingresa un número positivo.")
else:
    # Calculamos la suma de los números desde 0 hasta el número ingresado
    suma_total = sum(range(numero + 1))
    print(f"La suma de todos los números entre 0 y {numero} es: {suma_total}")

# Ejercicio Nro 8

def analizar_numeros(cantidad=100):  # La función acepta una cantidad de números configurable
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    print(f"Ingresa {cantidad} números enteros:")

    for _ in range(cantidad):  # Bucle para solicitar los números
        try:
            numero = int(input("Número: "))  # Convertimos la entrada a entero
            
            if numero % 2 == 0:  # Verifica si es par
                pares += 1
            else:  # Si no es par, es impar
                impares += 1
            
            if numero > 0:  # Verifica si es positivo
                positivos += 1
            elif numero < 0:  # Verifica si es negativo
                negativos += 1
            
        except ValueError:  # Maneja entradas inválidas
            print("Entrada inválida. Ingresa solo números enteros.")

    # Mostramos los resultados
    print("\nResultados:")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números positivos: {positivos}")
    print(f"Números negativos: {negativos}")

# Llamamos a la función, usando 100 como cantidad predeterminada
analizar_numeros()

# Ejercicio Nro 9

def calcular_media(cantidad=100):  # La función acepta una cantidad configurable de números
    suma_total = 0  # Variable para acumular la suma de los números
    
    print(f"Ingresa {cantidad} números enteros:")
    
    for _ in range(cantidad):  # Bucle para pedir los números al usuario
        try:
            numero = int(input("Número: "))  # Convertimos la entrada a entero
            suma_total += numero  # Sumamos el número ingresado
        except ValueError:  # Maneja entradas inválidas
            print("Entrada inválida. Ingresa solo números enteros.")

    # Calculamos la media dividiendo la suma total entre la cantidad de números ingresados
    media = suma_total / cantidad
    print(f"La media de los {cantidad} números ingresados es: {media}")

# Llamamos a la función, con 100 como cantidad predeterminada
calcular_media()

# Ejercicio Nro 10

# Pedimos al usuario un número entero
numero = input("Ingresa un número entero: ")  

# Invertimos el orden de los dígitos utilizando slicing
numero_invertido = numero[::-1]  

# Mostramos el resultado
print(f"El número invertido es: {numero_invertido}")