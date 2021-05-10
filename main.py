from Conjunto import claseConjunto
from Menu import claseMenu
import re
import os
def test():
    band = False
    lista = set()
    print('Conjunto 1: ')
    while not band:
        num = input('Número: ')
        if(re.match('^[0-9]{1,20}$', num.lower())):
            lista.add(int(num))
        else: print('ERROR: n° inválido')
        band = num.lower() == 'fin'
    conj1 = claseConjunto(lista)
    lista.clear()
    band = False
    print('Conjunto 2: ')
    while not band:
        num = input('Número: ')
        if(re.match('^[0-9]{1,20}', num.lower())):
            lista.add(int(num))
        else: print('ERROR: n° inválido')
        band = num.lower() == 'fin'
    conj2 = claseConjunto(lista)
    conj1.mostrar()
    conj2.mostrar()
if __name__ == '__main__':
    if(input('¿Testear?: ').lower() == 'si'):
        test()
    else:
        #variables
        band = False
        menu = claseMenu()
        #tareas
        menu.menu(0)
        while not band:
            print('|----MENU----|\n1. Unión de conjuntos\n2. Diferencia de conjuntos\n3. Comparación\n4. Salir')
            op = int(input('Opción: '))
            os.system('cls')
            menu.menu(op)
            band = op == 4