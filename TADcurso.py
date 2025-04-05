###### DEFINICION DE TAD COMPUESTO CURSO ######
#curso=[]

def crearCurso():
	#crea y retorna un curso vacío
	curso=[]
	return curso

def agregarEstudiante(curso, est):
	#agrega un estudiante al curso
	curso.append(est)
 
def eliminarEstudiante(curso, est):
	#elimina un estudiante del curso
	curso.remove(est)
 
def recuperarEstudiante(curso, i):
	#recupera el iesimo estudiante del curso
	return curso[i-1]

def tamanio(curso):
	#retorna la cantidad de estudiantes del curso
	return len(curso)