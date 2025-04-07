import TADestudiante

import TADcurso

from TADestudiante import *
from TADcurso import *
"""
curso1=crearCurso()

for i in range (1):
    est=crearEstudiante()
    nom=input("Ingrese el nombre\n")
    ap=input("Ingresa apellido\n")
    leg=input("Ingrese legajo\n")
    leg=int(leg)
    prom=input("Ingrese el promedio\n")
    prom=float(prom)
    cargarEstudiante(est,nom,ap,leg,prom)
    agregarEstudiante(curso1,est)


for i in range (1,tamanio(curso1)+1):
    recuperarEstudiante(curso1,tamanio(curso1))
    print(verNombre(est))
    print(verApellido(est))
    print(verLegajo(est))
    print(verPromedio(est))

"""

curso2=crearCurso()

sigue=1
while sigue == 1:
    est=crearEstudiante()
    nom=input("Ingrese el nombre\n")
    ap=input("Ingresa apellido\n")
    leg=input("Ingrese legajo\n")
    leg=int(leg)
    prom=input("Ingrese el promedio\n")
    prom=float(prom)
    cargarEstudiante(est,nom,ap,leg,prom)
    agregarEstudiante(curso2,est)
    print("Hay mas estudiantes? 1 - SI ")   
    sigue = int(input())

legajo=input("Ingrese el legajo del alumno a recuperar")
legajo=int(legajo)

for i in range (1,tamanio(curso2)+1):
    recuperarEstudiante(curso2,tamanio(curso2))

    if legajo == verLegajo(est):
        modPromedio(est,4)
        print(verNombre(est))
        print(verApellido(est))
        print(verPromedio(est))
    

legajo=input("Ingrese el legajo del alumno a eliminar")
legajo=int(legajo)

for i in range (1,tamanio(curso2)+1):
    recuperarEstudiante(curso2,tamanio(curso2))

    if legajo == verLegajo(est):
        print(verNombre(est))
        print(verApellido(est))
        eliminarEstudiante(curso2,est)
    
    else:
        print("No se encuentra el alumno ingresado")

