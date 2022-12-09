def mascara():
    print('''***MENU DE OPCIONES***'
    1.Lecturas recomendables:
    2.Películas recomendables:
    3.Discos recomendables:
    4.Videojuegos clásicos recomendables
    5.Salir''')
def lecturas():
    print('''Lecturas recomendables:
     + Esperándolo a Tito y otros cuentos de fúbol 
     + El juego de Ender (Orson Scott Card)
     + El sueño de los héroes (Adolfo Bioy Casares) ''')
def peliculas():
    print('''Películas recomendables:
     + Matrix (1999)
     + El último samuray (2003)
     + Cars (2006)''')
def discos():
    print('''Discos recomendables:
     + Despedazado por mil partes (La Renga, 1996)
     + Búfalo (La Mississippi, 2008)
     + Gaia (Mägo de Oz, 2003)''')
def videojuegos():
    print('''Videojuegos clásicos recomendables
     + Día del tentáculo (LucasArts, 1993)
     + Terminal Velocity (Terminal Reality/3D Realms, 
     + Death Rally (Remedy/Apogee, 1996)''')
def salir():
    print('''Gracias, vuelva prontos
    PROGRAMA FINALIZADO!!!''')
    print('=-'*20)
    
opc=1
while opc != 5 :
    mascara()
    opc=int(input('ingrese una opccion:'))
    if opc== 1:
        lecturas()
    elif opc== 2 :
        peliculas()
    elif opc== 3 :
        discos()
    elif opc== 4 :
        videojuegos()
    elif opc== 5 :
        salir()
    else : 
        print('ingrese una opcion valida:')
    
        
        