from funciones import *
palabras = [
    "elefante", "mariposa", "tigre", "delfin", "aguila", "ballena", 
    "reloj", "telescopio", "guitarra", "brujula", "espejo", "linterna", 
    "avioneta", "helicoptero", "velero", "tren", "globo aerostatico", 
    "submarino", "relampago", "cordillera", "oceano", "arrecife", 
    "bosque", "desierto", "libertad", "nostalgia", "valentia", 
    "sabiduria", "tiempo", "memoria"
]
def cont_exit(contador:int):
    diseñotext("BIENVENIDO","AL JUEGO DE PALABRAS","*")
    input()
    intentos("cuantos","oportunidades","desea?","*")
    oport = int(input("CANT: "))
    palabra = aleatorio(contador, palabras)
    print(palabra)

    while oport > 0:  
      contador += 1 
      print("hello")  
      oport -= 1


    print("Desea jugar de nuevo S/N: ")
    opcion = input()
    if opcion.lower() == "n":
        return 0
    elif opcion.lower() == "s":
        return cont_exit(contador+1)
    
    #aca nosotros empezamos con nuestro codigo de calcular la tarea
    
cont_exit(2)