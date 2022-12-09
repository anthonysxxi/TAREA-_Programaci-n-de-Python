def saludo():
    print('Hola mundo')
def doble(a):
    a = 2*a
    return(a)
def triple(b):
    b += 3*b
    return(b)
def mascara() :
    print('''***MENU OPCIONES***
1.Funcion saludo
2.Funcion doble(paso por valor)
3.Funcion triple(paso por referencia)''')
opc = 1
while opc != 4 :
    mascara()
    opc=int(input('ingrese una opcion:'))
    if opc == 1 :
        print('***llamada a la funcion saludo():***')
        saludo()
    elif opc == 2 :
        print('***llamada a la funcion doble:***')
        a=int(input('ingrese el valor de a:'))
        print('valor inicial:',a)
        print('valor modificado localmente:',doble(a))
        print('valor en la funcion principal:',a)
    elif opc == 3 :
        print('***llamada a la funcion triple:***')
        b=[int(input('ingrese 1er valor:')),int(input('ingrese el 2do valor:'))]
        print('valor inicial:',b)
        print('valor modificado localmente:',triple(b))
        print('valor en la funcion principal:',b)
    elif opc == 4 :
        print('***PROGRAMA FINALIZADO***')
    else :
        print('***ingrese una opcion valida***')