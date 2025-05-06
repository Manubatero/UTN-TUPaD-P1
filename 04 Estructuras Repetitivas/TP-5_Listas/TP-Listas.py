# Ejercicio N.° 1

# Usando comprensión de listas
multiplos_de_4 = list(range(4, 101, 4))

print(multiplos_de_4)  # Esto imprime la lista completa

# Ejercicio N.° 2

elementos = ["Notebook", "Bateria", "Libros", "Mate", "Asado"] # declaracion los cinco elelmentos para la lista.
print (elementos [-2]) # impresion por pantalla del penultimo elemento

# Ejercicio N.° 3

lista_vacia = [] # Lista vacia 
lista_vacia.append("Tamara") # Primera palabra agregada
lista_vacia.append("Gabriela") # Segunda palabra agregada
lista_vacia.append("Daiana") # Tercera palabra agregada
print(lista_vacia) # Impresion de la lista 

# Ejrcicio N.° 4

animales = ["perro", "gato", "conejo", "pez"] # Lista de animales
animales[1] = "loro" # Reemplazo del primer animal
animales[-1] = "oso" # Reemplazo del ultimo animal
print(animales) # impresion de la lista modificada 

# Ejercicio N.° 5

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# En este programa se declara la variable numeros con 5 numero al aplicar en la linea siguiente la funcion .remove (max) estamos eliminando el numero mas alto por eso que al imprimir el 22 que es el numero mas alto desaparece de la lista.

# Ejercicio N.° 6

numeros = [num for num in range(10, 31, 5)] # Declaracion de variable con numeros de 5 en 5
print (numeros[:2]) # Se imprime los 2 primeros por medio del slicing

# Ejercicio N.° 7

autos = ["sedan", "polo", "suran", "gol"] # Lista de autos
autos[1:3] = ["falcon", "corsa"] # modificaciones del indice 1 y 2
print(autos) # Se imprime la lista modificada 

# Ejercicio N.° 8 

dobles = [] # lista vacia 
dobles.append(10) # doble de 5
dobles.append(20) # doble de 10
dobles.append(30) # doble de 15
print(dobles) # Se imprime resultado 

# Ejerecicio N.° 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] # variable con los valores originales 
compras[2].append("jugo") # Se agrega un nuevo valor a la posicion 2 de la lista 
compras[1].remove("fideos") # Se elimina un valor de la posicion 1 de la lista 
compras[1].insert(1, "tallarines") # Se inserta un nuevo valor a la posicion 1 de la lista
compras[0].remove("pan") # Se elimina un valor de la posicion 0 de la lista
print(compras) # Se imprime lista actualizada 

# Ejercicio N.° 10

lista_anidada = [[], [], [], []] # Se crea lista anidada vacia
lista_anidada[0].append(15) # Se agrega el primer valor de la consigna a la posicion 0
lista_anidada[1].append(1==1) # Se agrega el segundo valor de la consigna a la posicion 1
lista_anidada[2].append(25.5) # Se agrega el tercer valor de la consigna a la posicion 2
lista_anidada[2].append(57.9) # Se agrega el cuarto valor de la consigna a la posicion 2
lista_anidada[2].append(30.6) # Se agrega el quinto valor de la consigna a la posicion 2
lista_anidada[3].append(2==1) # Se agrega el sexto valor de la consigna a la posicion 3
print(lista_anidada) # Se imprime lista con todos lo valores agregados.