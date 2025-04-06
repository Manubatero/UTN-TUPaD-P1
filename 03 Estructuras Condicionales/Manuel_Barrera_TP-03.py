#Ejercicio Nro 1
edad = int(input("Por favor, ingrese su edad: "))
if edad>18:
    print("Usted es mayor de edad")

#Ejercicio Nro 2
nota = float(input("Por favor, ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")

#Ejercicio Nro 3 
numero = int(input("Ingrese un numero par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un numero par")

#Ejercicio Nro 4
edad = int(input("Por favor, ingrese su edad: "))
if edad < 12:
    print("Pertenece a la categoria Niño/a")
elif 12 <= edad < 18:
    print("Pertenece a la categoria Adolecente")
elif 18 <= edad < 30:
    print("Pertenece a la categoria Adulto/a joven")
else:
    print("Pertenece a la categoria Adulto")

#Ejercicio Nro 5
contraseña = input("Por favor, ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio Nro 6
import random
import statistics
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
sesgo = "positivo" if media > mediana else "negativo" if media < mediana else "no hay sesgo"
print(f"Media: {media:.2f}, Mediana: {mediana:.2f}, Sesgo: {sesgo}")

#Ejercicio Nro 7
frase = input("Ingrese una palabra o texto: ")
if frase [-1].lower() in 'aeiou':
    frase += "!"
    print("Resultado:", frase)
else:
    print("Resultado:", frase)

#Ejercicio Nro 8
nombre = input("Ingrese su nombre: ")
print("Seleccione una opción:")
print("1 Convertir el nombre a mayúsculas")
print("2 Convertir el nombre a minúsculas")
print("3 Convertir el nombre con la primera letra en mayúscula")
opcion = int(input("Ingrese el número de la opción que desea (1, 2 o 3): "))
if opcion == 1:
    print("Resultado:", nombre.upper())
elif opcion == 2:
    print("Resultado:", nombre.lower())
elif opcion == 3:
    print("Resultado:", nombre.title())
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

#Ejercicio Nro 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#Ejercicio Nro 10
hemisferio = input("¿En cuál hemisferio te encuentras? (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1 para enero, 2 para febrero, etc.): "))
dia = int(input("Ingrese el número del día: "))
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"
print(f"Según la fecha ingresada, te encuentras en la estación: {estacion}")