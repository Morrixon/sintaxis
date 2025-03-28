#TAD (TIPO ABSTRACTO DE DATO)
#TADEstudiante

est=[Nombre,Apellido,Legajo,Promedio]
est=[" ",0,0]

#def crearEstudiante():
#crea un estudiante vacio

#def cargarEstudiante(Estudiante,nom,ape,leg,prom);
#inicializa estudiante con sus datos

#def asignarEstudiante(estudiante1,estudiante2);
#Asigna los datos del estudiante1 al estudiante2(copia al estudiante)

#------------EJERCICIO 1 DE CLASE -------------------

#Crear dos estudiante y cargarlos
#Imprimir los datos de cada estudiante al finalizar su respectiva carga
#Comparar los promedios e imprimir un cartel que diga que estudiante mayor promedio

#TAD

""" nom = "Chill"
print(nom)

apellido= input("Ingresa tu apellido de chill \n")

print(apellido)

numero= int(input("Ingrese un numero \n"))
print(numero) """


import TADEstudiante

from TADestudiante import *

est1= crearEstudiante():
est2=crearEstudiante():
nombre= input("ingrese el nombre \n")
apellido= input("ingrese apellido \n")
legajo=int(input("Ingrese el nro de legajo \n"))
nota=float(input("Ingrese la nota del alumno \n"))

cargarEst(est1,nombre,apellido,legajo,nota)

nombre= input("ingrese el nombre \n")
apellido= input("ingrese apellido \n")
legajo=int(input("Ingrese el nro de legajo \n"))
nota=float(input("Ingrese la nota del alumno \n"))

cargarEst(est2,nombre,apellido,legajo,nota)

nombre= input("ingrese el nombre \n")
apellido= input("ingrese apellido \n")
legajo=int(input("Ingrese el nro de legajo \n"))
nota=float(input("Ingrese la nota del alumno \n"))


#print(est1.nombre,est1.apellido,est1.legajo,est1.nota)


print(verNombre(est1))
print(verApellido(est1))
print(verLegajo(est1))
print(verPromedio(est1))

print(verNombre(est2))
print(verApellido(est2))
print(verLegajo(est2))
print(verPromedio(est2))




if(verProm(est1)>verProm(est2)):
    print("El estudiante de mayor promedio es el :",vernombre(est1))
else:
    print("El estudiante de mayor promedio es ",vernombre(est2))