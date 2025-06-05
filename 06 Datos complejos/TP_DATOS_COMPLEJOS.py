# Ejercicio N° 1

# Diccionario inicial con precios de algunas frutas
precios_frutas = {'banana': 1200, 'ananá': 2500, 'melón': 3000, 'uva': 1450}

# Agregar nuevas frutas con sus respectivos precios
precios_frutas['naranja'] = 1200
precios_frutas['manzana'] = 1500
precios_frutas['pera'] = 2300

# Imprimir el diccionario actualizado con todas las frutas y sus precios
print(precios_frutas)

# Ejercicio N° 2

# Actualizar los precios de algunas frutas en el diccionario
precios_frutas['banana'] = 1330
precios_frutas['manzana'] = 1700
precios_frutas['melón'] = 2800

# Imprimir el diccionario actualizado con los nuevos precios
print(precios_frutas)

# Ejercicio N° 3

# Obtener y mostrar solo los nombres de las frutas del diccionario
print(list(precios_frutas.keys()))

# Ejercicio N° 4

agenda = {}

# Cargar 5 contactos
for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[nombre] = telefono

# Consultar un número por nombre
consulta = input("Ingrese el nombre para buscar el número: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("El contacto no existe.")

# Ejercicio N° 5

# Solicitar la frase al usuario
frase = input("Ingrese una frase: ")

# Dividir la frase en palabras
palabras = frase.split()

# Obtener palabras únicas con un set
palabras_unicas = set(palabras)

# Contar la frecuencia de cada palabra
frecuencia_palabras = {}
for palabra in palabras:
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

# Imprimir los resultados
print(f"Palabras únicas: {palabras_unicas}")
print(f"Frecuencia de palabras: {frecuencia_palabras}")

# Ejercicio N° 6

# Crear un diccionario para almacenar los alumnos y sus respectivas notas
alumnos = {}

# Solicitar los nombres y las notas de 3 alumnos
for _ in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(map(float, input("Ingrese tres notas separadas por espacio: ").split()))
    alumnos[nombre] = notas

# Calcular y mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")

# Ejercicio N° 7

# Definir los sets de estudiantes que aprobaron cada parcial
parcial_1 = {"Ana", "Carlos", "Miguel", "Sofía", "Lucas"}
parcial_2 = {"Carlos", "Miguel", "Valeria", "Lucas", "Fernanda"}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos_parciales = parcial_1 & parcial_2
print(f"Estudiantes que aprobaron ambos parciales: {ambos_parciales}")

# Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = parcial_1 ^ parcial_2
print(f"Estudiantes que aprobaron solo uno de los dos parciales: {solo_uno}")

# Lista total de estudiantes que aprobaron al menos un parcial (unión)
total_aprobados = parcial_1 | parcial_2
print(f"Lista total de estudiantes que aprobaron al menos un parcial: {total_aprobados}")

# Ejercicio N° 8

# Crear un diccionario vacío para almacenar productos y su stock
stock_productos = {}

while True:
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print("El producto no existe en el inventario.")

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock_productos:
            unidades = int(input("Ingrese la cantidad a agregar: "))
            stock_productos[producto] += unidades
            print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print("El producto no existe. Primero agrégalo como nuevo.")

    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto in stock_productos:
            print("El producto ya existe. Use la opción de agregar unidades.")
        else:
            unidades = int(input("Ingrese la cantidad inicial de stock: "))
            stock_productos[producto] = unidades
            print(f"Producto {producto} agregado con {unidades} unidades.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intente nuevamente.")

# Ejercicio N° 9

# Crear un diccionario vacío para la agenda
agenda = {}

# Cargar eventos en la agenda
for _ in range(3):  # Puedes cambiar el número de eventos a ingresar
    dia = input("Ingrese el día del evento: ")
    hora = input("Ingrese la hora del evento: ")
    evento = input("Ingrese el nombre del evento: ")
    agenda[(dia, hora)] = evento

# Consultar un evento según día y hora
dia_consulta = input("Ingrese el día a consultar: ")
hora_consulta = input("Ingrese la hora a consultar: ")

# Verificar si hay un evento programado en esa fecha y hora
if (dia_consulta, hora_consulta) in agenda:
    print(f"El evento programado en {dia_consulta} a las {hora_consulta} es: {agenda[(dia_consulta, hora_consulta)]}")
else:
    print("No hay eventos programados en ese horario.")

# Ejercicio N° 10

# Diccionario original con países como claves y capitales como valores
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Japón": "Tokio"
}

# Invertir el diccionario para que las capitales sean claves y los países valores
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

# Imprimir el nuevo diccionario
print(capitales_paises)