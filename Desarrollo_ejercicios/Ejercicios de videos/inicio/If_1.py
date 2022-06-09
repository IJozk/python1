print("Programa de evaluacion de notas de alumnos")

nota_alumno=input("Intrduce la nota del alumno: ")
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="reprobado"
    return valoracion
        
print(evaluacion(int(nota_alumno)))