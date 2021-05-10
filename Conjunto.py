import re
class claseConjunto:
    __conj = set()
    def __init__(self, lista):
        self.__conj = lista.copy()
    def mostrar(self):
        print(self.__conj)
    def getConj(self):
        return self.__conj
    def __add__(self, other):
        return claseConjunto(self.__conj | other.getConj())
    def __sub__(self, other):
        return claseConjunto(self.__conj & other.getConj())
    def __eq__(self, other):
        return self.__conj == other.getConj()