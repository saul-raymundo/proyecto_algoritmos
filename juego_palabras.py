from funciones.py import *

def cont_exit():
    




    print("Desea jugar de nuevo S/N: ")
    opcion = input()
    if opcion.lower() == "n":
        return 0
    elif opcion.lower() == "s":
        return cont_exit()
    
    #aca nosotros empezamos con nuestro codigo de calcular la tarea
    
cont_exit()