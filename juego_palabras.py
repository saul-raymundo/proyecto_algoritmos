#importamos funciones de otro modulo 
from funciones import *
#crear una lista de palabras aleatorias
palabras = [
    "elefante", "mariposa", "tigre", "delfin", "aguila", "ballena", 
    "reloj", "telescopio", "guitarra", "brujula", "espejo", "linterna", 
    "avioneta", "helicoptero", "velero", "tren", "globo aerostatico", 
    "submarino", "relampago", "cordillera", "oceano", "arrecife", 
    "bosque", "desierto", "libertad", "nostalgia", "valentia", 
    "sabiduria", "tiempo", "memoria"
]
#funcion para evaluar el progreso de la palabra y actualizarla
def progreso(lista,palabra,letra):
    #aca nosotros buscamos la letra en la palabra y a ala vez su indice para actualizarla
    for indi,carac in enumerate(palabra):
        if carac == letra:
            #actualiza el espacio y la cambia de # por la letra correcta
            lista[indi]=letra
    #devuelve la lista en formato de cadena        
    return "".join(lista)

#funcion para validar que realmente pertenece a la cadena
def pertenece(letra,palabra):
    if  letra.lower() in palabra:
        textree("CORRECTO!!", f"LA LETRA '{letra}'","SI EXISTE EN LA PALABRA","*")
        input("ENTER para continuar -->")
        return True
        
    else:
        #se ejecuta cuando no existe en la palabra
        textree("ERROR!!",f"LA LETRA '{letra}'","NO ExISTE EN LA PALABRA","*")
        input("ENTER para continuar -->")
        return False

   #funcion para ver si la palabra ya esta completa para hacerselo saber al usuario 
def encont_pala(progreso,palabra):
    if progreso == palabra: # validamos si el usuario a completado la palabra
        textree("¡GANASTE!","la palaba era: ",palabra,"*")
        input("ENTER para continuar -->")
        return True
    else:
        return False 
#funcion recursiva que si el usuario dice que quiere volver regresa pero con un contador distinto
# el cual sirve para que en cada vuelta este cambie de palabra sin usar la biblioteca ramdom         
def cont_exit(contador:int):
    while True:
        diseñotext("BIENVENIDO","AL JUEGO DE PALABRAS","*")
        input("ENTER para continuar -->")
        textree("cuantas","oportunidades","desea?","*")
        oport = input("--> ").strip()
        #definido por si el valor del usuario al convertirlo a int da error entonces salte un mensaje amigable y no bloquea
        try:
            oport = int(oport)
            #validamos si el valor es mayor a cero para empezar con el programa
            if oport > 0:
                #utilizamos la funcion que es como un ramdon pero a mi modo
                palabra = aleatorio(contador, palabras)
                cartnum =["#"]* len(palabra)
                print(palabra)
                #muestra la palabra en un texto personalizado con bordes
                textree("la palabraoculta es: ","".join(cartnum),f"tiene {len(palabra)} letras","*")
                input("ENTER para continuar -->")
                #se ejecuta el cilo si las oportunidades del usuario son mayores a cero
                while oport > 0:  
                    letra = input(textree("INGRESE","UNA","LETRA","*")).strip()
                    #la condicion significa que si el usuario ingresa una sola letra entonces se ejecuta si no es error. 
                    if len(letra) == 1:
                        valbool=pertenece(letra,palabra)#devuelve un valor booleno que si la letra pertenece es True.
                        #si es True se ejecuta este bloque
                        if valbool:
                            #inplemento la funcion para ir actualizando el progreso de la palabra
                            progress = progreso(cartnum,palabra,letra)
                            #agregamos a una funcion de texto personalizado
                            diseñotext("PROGRESO",progress,"*")
                            input("ENTER para continuar -->")#para pasar al siguiente luego de dar un enter
                            #para validar si la palabra ya esta completa: 
                            result = encont_pala(progress,palabra)
                            if result:
                                #salir si la palabra se completo
                                break
                            else:
                                #continuar por si aun falta
                                continue
                           
                        else: #si es false (la letra no pertenece a la palabra)
                          oport -= 1
                          if oport == 0:
                                #muesta el mensaje si al usuario ya agoto sus vidas
                                mensj_pers("PERDISTE",");","LA PALABRA",f"ERA: {palabra}","","*")
                                input("ENTER para continuar -->") 
                            #se ejecuta si el usuario aun le quedan oportunidades     
                          else:
                                diseñotext("OPORTUNIDADES",f"RESTANTES {oport}","*")
                                input("ENTER para continuar -->")  

                    #si el usuario ingresa mas de dos letras o valores a la vez no vale    
                    else:
                        mensj_pers("ERROR!!","INGRESE","UN","UNICO","VALOR","*")
                        input("ENTER para continuar -->")
                        textree("INTENTAMOS","DE NUEVO?","S/N","*")
                        opcion = input("-->").strip()
                        #condicion que funciona para reiniciar el programa otra vez
                        if opcion.lower() == "n":
                            textree("GRACIAS","POR","JUGAR","*")
                            return 0
                        elif opcion.lower() == "s":
                            return cont_exit(contador+1)
                        
                #se ejecuta si al usuaio ya no le quedan mas oportunidades, (ya agoto todas)
                textree("JUGAMOS","DE NUEVO?","S/N","*")
                opcion = input("-->").strip()
                if opcion.lower() == "n":
                    textree("GRACIAS","POR","JUGAR","*")
                    break
                elif opcion.lower() == "s":
                    return cont_exit(contador+1)
            #este bloque se ejecuta si el valor asignado es menor a cero    
            else:
                mensj_pers("POR FAVOR","INGRESA","VALORES","MAYORES A","CERO (0)","*")
                input("ENTER para continuar -->")

        #se ejecuta si el valor del usuario no es entero y lanza una excepcion pero ya la tenemos controlada
        except ValueError:
            mensj_pers("ERROR!!","POR FAVOR","INGRESA VALORES","NUMERICOS Y ENTEROS","!!","*")
            input("ENTER para continuar -->")

#este contador cambiara cada vez que ejecutemos el programa porque nos da un valor unico segun la RAM
contador = id(object())
cont_exit(contador)