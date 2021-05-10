from Conjunto import claseConjunto
import re
class claseMenu:
    __conj1 = None
    __conj2 = None
    def menu(self, op):
        if(op == 0):    #crea los conjuntos
            band = False
            conj = set()
            print('|----CREAR CONJUNTOS----|\nDATO: "fin" para finalizar el ingreso\nConjunto 1: ')
            while not band:
                num = input('Número: ')
                if(re.match('^[0-9]{1,20}$', num.lower())):
                    conj.add(int(num))
                else: print('ERROR: n° inválido')
                band = num.lower() == 'fin'
            self.__conj1 = claseConjunto(conj)
            conj.clear()
            band = False
            print('Conjunto 2:')
            while not band:
                num = input('Número: ')
                if(re.match('^[0-9]{1,20}$', num.lower())):
                    conj.add(int(num))
                else: print('ERROR: n° inválido')
                band = num.lower() == 'fin'
            self.__conj2 = claseConjunto(conj)
            conj.clear()
            self.__conj1.mostrar()
            self.__conj2.mostrar()
        elif(op == 1):  #unión de los conjuntos
            print('|----UNIÓN DE LOS CONJUNTOS----|')
            union = self.__conj1 + self.__conj2
            union.mostrar()
            input()
        elif(op == 2):  #diferencia de los conjuntos
            print('|----DIREFENCIA DE LOS CONJUNTOS----|')
            dif = self.__conj1 - self.__conj2
            dif.mostrar()
            input()
        elif(op == 3):  #comparación de los conjuntos
            print('|----IGUALDAD DE CONJUNTOS----|')
            eq = self.__conj1 == self.__conj2
            print('Resultado: ', eq)
            input()
        elif(op == 4):
            print('DATO: finalizando...')
        else: print('ERROR: opción inválida')