# Funciones con Args


def suma(*args):

    resultado = 0
    for n in args:
        resultado += n
    print('El resultado es: '+str(resultado))
    
    


    
suma(5,9,8)
suma(5,9)
suma(5,5)
suma(10,15,15,16,18,19,20)