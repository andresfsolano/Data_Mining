#Algoritmo que carga un archivo tipo CSV, calcula el promedio de la edad, además identifica la edad mínima y máxima.

#Se importa el módulo CSV y se crean variables que posteriormente se usarán.
import csv
listofages = list()
sumofages = 0
registers = 0

file = input("Ingrese el nombre del archivo tipo CSV: ")

#Se abre el archivo y se emplea la función reader que lo recorre línea a línea.
f = open(file)
filereader = csv.reader(f)

#Se toma la posición 1 (realmente sería la columna 2), donde se agregan las edades a una lista.
for row in filereader:
    numbers = row[1]
    listofages.append(numbers)

#Se elimina el primer elemento de la lista ("Ages"). Posteriormente, se convierte todos los elementos de la lista a punto flotante (float).
del listofages[0]
listofages = [float(i) for i in listofages]
print("Las edades de los pacientes son:", listofages)

#Se halla el promedio, a partir de la suma de las edades entre el número total de registros.
for n in listofages:
    sumofages = sumofages + n
    registers = registers + 1
meanofages = sumofages/registers

print("El número total de registros es igual a",registers)
print()
print("La suma de las edades es igual a",round(sumofages,3))
print("El promedio de las edades es",round(meanofages,3))
print("La edad mínima es", min(listofages))
print("La edad máxima es", max(listofages))