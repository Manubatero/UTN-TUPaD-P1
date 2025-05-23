# Ejercicio N° 1 

#Definicion de la funcion
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

# Ejercicio N° 2

# Definicion de funcion
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Solicitar el nombre al usuario
nombre_usuario = input("Ingresa tu nombre: ")

# Programa principal
print(saludar_usuario(nombre_usuario))

# Ejercicio N° 3

# Definicion de funcion
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

# Solicitar el  al datos
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
lugar = input("Ingresa tu lugar de residencia: ")

# Programa principal
print(informacion_personal(nombre, apellido, edad, lugar))

# Ejercicio N° 4

import math  # Importamos el módulo math

# Definicion de Funciones
def calcular_area_circulo(radio):
    return math.pi * radio ** 2  # Fórmula del área

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio  # Fórmula del perímetro

# Solicitar el radio al usuario
radio = float(input("Ingresa el radio del círculo: "))

# Programa principal
print(f"Área del círculo: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio):.2f}")

# Ejercicio N° 5

# Definicion de funcion
def segundos_a_horas(segundos):
    return segundos // 3600

# Solicitar segundos al usuario
segundos = int(input("Por favor los segundos: "))

# Programa Principal
print(f"La cantida de horas es: {segundos_a_horas(segundos)}")

# Ejercicio N° 6

# Definimos funciones
def tabla_multiplicar(numero):
    i = 1
    while i <= 10:  # Creamos ciclo While
        print(f"{numero} x {i} = {numero * i}")  
        i += 1 

# Solicitamos un numero al usuario
numero = int(input("Ingrese un número del 1 al 10: "))

# Programa principal
tabla_multiplicar(numero)

# Ejercicio N° 7

# Definicion de funcion
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a // b if b != 0 else "Indefinido"
    return (suma, resta, multiplicacion, division)

# Solicitar números al usuario
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(a, b)

# Programa principal
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"Division: {resultados[3]}")

# Ejercicio N° 8

# Definicion de funcion
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicitar datos al usuario
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Programa principal
print(f"Tu IMC es: {calcular_imc(peso, altura):.2f}")

# Ejercicio N° 9

# Definicion de funcion
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32  

# Solicitar temperatura al usuario
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Mostrar el resultado usando la funcion
print(f"La temperatura en Fahrenheit es: {celsius_a_fahrenheit(celsius):.2f}")

# Ejercicio N° 10

# Definicion de funcion
def calcular_promedio(a, b, c):
    return (a + b + c) / 3 

# Solicitar numeros al usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

# Programa principal
print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")