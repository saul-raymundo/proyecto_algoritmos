from funciones import *
palabras = [
    "elefante", "mariposa", "tigre", "delfin", "aguila", "ballena", 
    "reloj", "telescopio", "guitarra", "brujula", "espejo", "linterna", 
    "avioneta", "helicoptero", "velero", "tren", "globo aerostatico", 
    "submarino", "relampago", "cordillera", "oceano", "arrecife", 
    "bosque", "desierto", "libertad", "nostalgia", "valentia", 
    "sabiduria", "tiempo", "memoria"
]
def cont_exit():
    diseñotext("BIENVENIDO","AL JUEGO DE PALABRAS","*")
    input()
    intentos("cuantos","oportunidades","desea?","*")
    oport = int(input("CANT: "))
    while oport > 0:
        


    print("Desea jugar de nuevo S/N: ")
    opcion = input()
    if opcion.lower() == "n":
        return 0
    elif opcion.lower() == "s":
        return cont_exit()
    
    #aca nosotros empezamos con nuestro codigo de calcular la tarea
    
cont_exit()