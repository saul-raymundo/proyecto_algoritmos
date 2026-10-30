def diseñotext(text1,text2,marco):
    arrib = (marco.ljust(50,marco))#son los marcos de arriba
    i = 0
    print(arrib)
    while True:
        forma = (marco+ " " * 49 + marco)#esta agrega los "*" a los costados mientras tiene 49 espacios dentro
        print(forma)
        i +=1
        if i == 1:#siginifica que luego de dos lineas de espacios con asterisco se ejecuta lo siguiente
            inf = text1.center(47)
            inf2 = text2.center(47)
            print(marco,inf,marco)
            print(marco,inf2,marco)
            print(forma+'\n'+ arrib)#aca agrega dos enter y luego muestra el marco de abajo del recuadro
            return 0




   
    