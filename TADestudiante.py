###### DEFINICION DE TAD SIMPLE ESTUDAINTE ######

estudiante = ["","",0,0]
    #nombre,apellido,legajo,promedio

def crearEstudiante():
    #crea un estudiante vacio
    estudiante = ["","",0,0]
    return estudiante

def cargarEstudiante(estudiante,nom,ap,leg,prom):
    #carga un nuevo estudiante
    #[#nombre,apellido,legajo,promedio]
    estudiante[0]=nom
    estudiante[1]=ap
    estudiante[2]=leg
    estudiante[3]=prom

def asignarEstudiante(estudiante1,estudiante2):
    #copia los datos del estudiante1 al estudiante2
    estudiante2[0]=estudiante1[0]
    estudiante2[1]=estudiante1[1]
    estudiante2[2]=estudiante1[2]
    estudiante2[3]=estudiante1[3]

def verNombre(estudiante):
    #Retorna el nombre del estudiante
    return estudiante[0]

def verApellido(estudiante):
    #Retorna el apellido del estudiante
    return estudiante[1]

def verLegajo(estudiante):
    #Retorna el legajo del estudiante
    return estudiante[2]

def verPromedio(estudiante):
    #Retorna el promedio del estudiante
    return estudiante[3]

def modNombre(estudiante, nuevoNom):
    #Modifica el nombre del estudiante
    estudiante[0] = nuevoNom

def modApellido(estudiante, nuevoApe):
    #Modifica el apellido del estudiante
    estudiante[1] = nuevoApe

def modLegajo(estudiante, nuevoLeg):
    #Modifica el legajo del estudiante
    estudiante[2] = nuevoLeg

def modPromedio(estudiante, nuevoProm):
    #Modifica el promedio del estudiante
    estudiante[3] = nuevoProm
