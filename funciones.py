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

def textree(tex1,tex2,tex3,mards):
    arrib_ab = (mards.ljust(50,mards))
    print(arrib_ab)
    i = 0
    while True:
        forma = (mards+ " " * 49 + mards)#esta agrega los "*" a los costados mientras tiene 49 espacios dentro
        print(forma)
        i +=1
        if i == 1:#siginifica que luego de dos lineas de espacios con asterisco se ejecuta lo siguiente
            inf = tex1.center(47)
            inf2 = tex2.center(47)
            inf3 = tex3.center(47)
        print(mards,inf,mards)
        print(mards,inf2,mards)
        print(mards,inf3,mards)
        print(forma+'\n'+ arrib_ab)#aca agrega dos enter y luego muestra el marco de abajo del recuadro
        return 0

def aleatorio(contador,lista):
    salto = 2
    indice = (contador * salto) % len(lista)
    return lista[indice]


def mensj_eror(tex1,tex2,tex3,tex4,tex5,borde):
    arrib_ab = (borde.ljust(50,borde))
    print(arrib_ab)
    i = 0
    while True:
        forma = (borde+ " " * 49 + borde)#esta agrega los "*" a los costados mientras tiene 49 espacios dentro
        print(forma)
        i +=1
        if i == 1:#siginifica que luego de dos lineas de espacios con asterisco se ejecuta lo siguiente
            ms1 = tex1.center(47)
            ms2 = tex2.center(47)
            ms3 = tex3.center(47)
            ms4 = tex4.center(47)
            ms5 = tex5.center(47)
        print(borde,ms1,borde)
        print(borde,ms2,borde)
        print(borde,ms3,borde)
        print(borde,ms4,borde)
        print(borde,ms5,borde)
        print(forma+'\n'+ arrib_ab)#aca agrega dos enter y luego muestra el marco de abajo del recuadro
        return 0





   
    