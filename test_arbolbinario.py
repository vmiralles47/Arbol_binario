# de momento crea y pinta el arbol del reto
# recorre el arbol y el __str__ representa las inserciones en orden ascendente

from arbol_binario import Nodo_bin, Arbol_bin

arbol = Arbol_bin(Nodo_bin(5))
print(arbol)

arbol.inserta_nodo(Nodo_bin(3))
print(arbol)

arbol.inserta_nodo(Nodo_bin(7))
print(arbol)

arbol.inserta_nodo(Nodo_bin(2))
print(arbol)

arbol.inserta_nodo(Nodo_bin(4))
print(arbol)

arbol.inserta_nodo(Nodo_bin(1))
print(arbol)

arbol.inserta_nodo(Nodo_bin(10))
print(arbol)

arbol.inserta_nodo(Nodo_bin(9))
print(arbol)
