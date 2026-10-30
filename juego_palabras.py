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
    while True:
        diseñotext("BIENVENIDO","AL JUEGO DE PALABRAS","*")
        input()
        textree("cuantos","oportunidades","desea?","*")
        oport = input("--> ")
        try:
            oport = int(oport)
            if oport > 0:
                palabra = aleatorio(contador, palabras)
                cartnum =["#"]* len(palabra)
                print(palabra)
                print(f"La palabra oculta: "+"".join(cartnum)+f" tiene {len(palabra)} letras ")
        
                while oport > 0:  
                    letra = input(textree("INGRESE","UNA","LETRA","*"))
                    if len(letra) == 1:
                        if letra.lower() in palabra:
                            print(f"\n¡CORRECTO!, la letra '{letra}' si existe en la palabra \n")
                            for indi,carac in enumerate(palabra):
                                if carac == letra:
                                    cartnum[indi]=letra
                                    print("".join(cartnum))
                        else:
                            print(f"\nERROR!!, la letra  '{letra}' No existe en la palabra")
                            oport -= 1
                            print(f"oportunidades restantes {oport}\n")
        
                        busca_usu = "".join(cartnum) 
                        if busca_usu == palabra:
                            textree("correcto","la palaba es: ",busca_usu,"*")
                            break
                        else:
                            continue
                    else:
                        mensj_eror("ERROR!!","INGRESE","UN","UNICO","VALOR")
                        textree("INTENTAMOS","DE NUEVO?","S/N","*")
                        opcion = input("-->")
                        if opcion.lower() == "n":
                            textree("GRACIAS","POR","JUGAR","*")
                            return 0
                        elif opcion.lower() == "s":
                            return cont_exit(contador+1)
                
                textree("JUGAMOS","DE NUEVO?","S/N","*")
                opcion = input("-->")
                if opcion.lower() == "n":
                    textree("GRACIAS","POR","JUGAR","*")
                    break
                elif opcion.lower() == "s":
                    return cont_exit(contador+1)
            else:
                mensj_eror("POR FAVOR","INGRESA","VALORES","MAYORES A","CERO (0)","*")
            
        except ValueError:
            mensj_eror("ERROR!!","POR FAVOR","INGRESA VALORES","NUMERICOS Y ENTEROS","!!","*")
            input()

#este contador cambiara cada vez que ejecutemos el programa porque nos da un valor unico segun la RAM
contador = id(object())
cont_exit(contador)