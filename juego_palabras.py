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
    cartnum =["#"]* len(palabra)
    print(palabra)
    print(f"La palabra: "+"".join(cartnum)+f" La palabra tiene {len(palabra)} letras ")

    while oport > 0:  
      letra = input("INGRESA UNA LETRA: ")
      
      if letra.lower() in palabra:
        print(f"\n¡CORRECTO!, la letra '{letra}' si existe en la palabra \n")
        
        for indi,carac in enumerate(palabra):
           #if 
            if carac == letra:
              cartnum[indi]=letra
              print("".join(cartnum))
      else:
        print(f"\nERROR!!, la letra  '{letra}' No existe en la palabra")
        oport -= 1
        print(f"oportunidades restantes {oport}\n")

      busca_usu = "".join(cartnum) 
      if busca_usu == palabra:
        intentos("correcto","la palaba es: ",busca_usu,"*")
        break
      else:
        continue
      
    print("Desea jugar de nuevo S/N: ")
    opcion = input()
    if opcion.lower() == "n":
        intentos("GRACIAS","POR","JUGAR","*")
        return 0
    elif opcion.lower() == "s":
        return cont_exit(contador+1)
    
#este contador cambiara cada vez que ejecutemos el programa porque nos da un valor unico segun la RAM
contador = id(object())
cont_exit(contador)