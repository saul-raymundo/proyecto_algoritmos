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
        input("ENTER para continuar -->")
        textree("cuantas","oportunidades","desea?","*")
        oport = input("--> ").strip()
        try:
            oport = int(oport)
            if oport > 0:
                palabra = aleatorio(contador, palabras)
                cartnum =["#"]* len(palabra)
                print(palabra)
                textree("la palabraoculta es: ","".join(cartnum),f"tiene {len(palabra)} letras","*")
                input("ENTER para continuar -->")
                while oport > 0:  
                    letra = input(textree("INGRESE","UNA","LETRA","*")).strip()
                    if len(letra) == 1:
                        if letra.lower() in palabra:
                            textree("CORRECTO!!", f"LA LETRA '{letra}'","SI EXISTE EN LA PALABRA","*")
                            input("ENTER para continuar -->")
                            for indi,carac in enumerate(palabra):
                                if carac == letra:
                                    cartnum[indi]=letra
                            diseñotext("PROGRESO: ","".join(cartnum),"*")
                            input("ENTER para continuar -->")
                        else:
                            textree("ERROR!!",f"LA LETRA '{letra}'","NO ExISTE EN LA PALABRA","*")
                            input("ENTER para continuar -->")
                            oport -= 1
                            diseñotext("OPORTUNIDADES",f"RESTANTES {oport}","*")
                            input("ENTER para continuar -->")
        
                        busca_usu = "".join(cartnum) 
                        if busca_usu == palabra:
                            textree("correcto","la palaba es: ",busca_usu,"*")
                            input("ENTER para continuar -->")
                            break
                        else:
                            continue
                    else:
                        mensj_pers("ERROR!!","INGRESE","UN","UNICO","VALOR")
                        input("ENTER para continuar -->")
                        textree("INTENTAMOS","DE NUEVO?","S/N","*")
                        opcion = input("-->").strip()
                        if opcion.lower() == "n":
                            textree("GRACIAS","POR","JUGAR","*")
                            return 0
                        elif opcion.lower() == "s":
                            return cont_exit(contador+1)
                
                textree("JUGAMOS","DE NUEVO?","S/N","*")
                opcion = input("-->").strip()
                if opcion.lower() == "n":
                    textree("GRACIAS","POR","JUGAR","*")
                    break
                elif opcion.lower() == "s":
                    return cont_exit(contador+1)
            else:
                mensj_pers("POR FAVOR","INGRESA","VALORES","MAYORES A","CERO (0)","*")
                input("ENTER para continuar -->")
            
        except ValueError:
            mensj_pers("ERROR!!","POR FAVOR","INGRESA VALORES","NUMERICOS Y ENTEROS","!!","*")
            input("ENTER para continuar -->")

#este contador cambiara cada vez que ejecutemos el programa porque nos da un valor unico segun la RAM
contador = id(object())
cont_exit(contador)