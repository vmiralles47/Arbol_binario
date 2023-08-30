"""
meter valores de uno en uno
el primero será la raíz y todo se recorrerá en relación a ella
el arbol está formado de nodos binarios, y tiene métodos para insertar, buscar, borrar y mostrarlo, que requerirán a su vez
métodos para recorrerlo
cada Nodo_bin tiene un valor y dos hijos, el menor y el mayor
"""


class Nodo_bin():

    def __init__(self, valor):
        self.valor = valor
        self.hijo_menor = None
        self.hijo_mayor = None

    def __str__(self):
        return f"NODO {self.valor} -- [{self.hijo_menor} - {self.hijo_mayor}]"

    def __repr__(self):
        return self.__str__()


class Arbol_bin():

    def __init__(self, nodo):
        if not isinstance(nodo, Nodo_bin):
            raise ValueError("el nodo raíz debe ser un nodo binario")
        else:
            self.raiz = nodo

    def __str__(self):
        return f"arbol {self.raiz}"

    def __repr__(self):
        return self.__str__()

    def inserta_nodo(self, nodo_a_insertar):
        if not isinstance(nodo_a_insertar, Nodo_bin):
            raise ValueError("debes insertar un nodo binario")
        else:
            # recorre el arbol hacia abajo desde la raíz y busca el sitio de inserción
            nodo_donde_insertar = self.busca_nodo_de_insercion(
                self.raiz, nodo_a_insertar)
            print("insertando en ", nodo_donde_insertar)
            # inserta_nodo
            if nodo_a_insertar.valor < nodo_donde_insertar.valor:
                nodo_donde_insertar.hijo_menor = nodo_a_insertar
            else:
                nodo_donde_insertar.hijo_mayor = nodo_a_insertar

            print("insertado en ", nodo_donde_insertar)

    def busca_nodo_de_insercion(self, nodo_de_partida, nodo_a_insertar):
        nodo_de_insercion = Nodo_bin(0)  # cualquier valor para inicializar

        # empieza en la raiz:
        nodo_actual = nodo_de_partida

        if nodo_a_insertar.valor == nodo_actual.valor:
            raise ValueError("el número ya existe, no se puede insertar")
        else:
            # se va por la izquierda(hijo menor)
            if nodo_a_insertar.valor < nodo_actual.valor:
                if nodo_actual.hijo_menor is None:
                    nodo_de_insercion = nodo_actual
                    return nodo_de_insercion
                else:
                    nodo_actual = nodo_actual.hijo_menor
                    return self.busca_nodo_de_insercion(
                        nodo_actual, nodo_a_insertar)  # llamada recursiva
            else:  # se va por la derecha (hijo mayor)
                if nodo_actual.hijo_mayor is None:
                    nodo_de_insercion = nodo_actual
                    return nodo_de_insercion
                else:
                    nodo_actual = nodo_actual.hijo_mayor
                    return self.busca_nodo_de_insercion(
                        nodo_actual, nodo_a_insertar)  # llamada recursiva?

    # def agrega_nodo(nodo_a_insertar, nodo_donde_insertar):
