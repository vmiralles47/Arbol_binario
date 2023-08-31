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
        return f"NODO {self.valor} --  [{self.hijo_menor} - {self.hijo_mayor}]"

    def __repr__(self):
        return self.__str__()


class Arbol_bin():

    def __init__(self, nodo):
        if not isinstance(nodo, Nodo_bin):
            raise ValueError("el nodo raíz debe ser un nodo binario")
        else:
            self.raiz = nodo

        self.lista_valores = [nodo.valor]
        self.lista_valores_asc = [0]
        self.lista_valores_desc = [0]

    def __str__(self):
        self.lista_valores_asc = [0]
        self.valor_asc(self.raiz)
        return f"arbol {self.lista_valores_asc}"

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
    """""
    def tiene_nietos (self, nodo):
       return (
           nodo.hijo_menor.hijo_menor is not None 
           or 
           nodo.hijo_menor.hijo_mayor is not None 
           or 
           nodo.hijo_mayor.hijo_menor is not None 
           or 
           nodo.hijo_mayor.hijo_menor is not None)
    """

    def agrega_valor(self, valor):
        if self.lista_valores_asc == [0]:
            self.lista_valores_asc[0] = valor
        else:
            self.lista_valores_asc.append(valor)

    def valor_asc(self, nodo):
        nodo_actual = nodo
       # nodo sin hijos
        if nodo_actual.hijo_menor is None and nodo_actual.hijo_mayor is None:
            self.agrega_valor(nodo.valor)
            return self.lista_valores_asc
        # nodo con hijo_menor y NO hijo_mayor - bajamos de nivel x la izquierda
        if nodo_actual.hijo_menor is not None and nodo_actual.hijo_mayor is None:
            nodo_actual = nodo_actual.hijo_menor
            self.valor_asc(nodo_actual)
            nodo_actual = nodo
            self.agrega_valor(nodo_actual.valor)
            return self.lista_valores_asc

        # nodo sin hijo menor y con hijo mayor - guardamos el valor y bajamos de nivel por la derecha
        if nodo_actual.hijo_menor is None and nodo_actual.hijo_mayor is not None:
            self.agrega_valor(nodo_actual.valor)
            nodo_actual = nodo_actual.hijo_mayor
            self.valor_asc(nodo_actual)

            return self.lista_valores_asc
        # nodo con ambos hijos: bajamos por la izq , guardamos el valor del nodoy bajamos por la dcha
        if nodo_actual.hijo_menor is not None and nodo_actual.hijo_mayor is not None:
            nodo_actual = nodo_actual.hijo_menor
            self.valor_asc(nodo_actual)
            nodo_actual = nodo
            self.agrega_valor(nodo_actual.valor)
            nodo_actual = nodo_actual.hijo_mayor
            self.valor_asc(nodo_actual)
            return self.lista_valores_asc

    def agrega_valor_desc(self, valor):
        if self.lista_valores_desc == [0]:
            self.lista_valores_desc[0] = valor
        else:
            self.lista_valores_desc.append(valor)

    def valor_desc(self, nodo):
        nodo_actual = nodo
        # nodo sin hijos
        if nodo_actual.hijo_menor is None and nodo_actual.hijo_mayor is None:
            self.agrega_valor_desc(nodo.valor)
            return self.lista_valores_desc

        # nodo con ambos hijos: bajamos por la derecha ,luego  guardamos el valor del nodo y bajamos por la izqd
        if nodo_actual.hijo_menor is not None and nodo_actual.hijo_mayor is not None:
            nodo_actual = nodo_actual.hijo_mayor
            self.valor_desc(nodo_actual)
            nodo_actual = nodo
            self.agrega_valor_desc(nodo_actual.valor)
            nodo_actual = nodo_actual.hijo_menor
            self.valor_desc(nodo_actual)
            return self.lista_valores_desc

        # nodo con hijo_menor y NO hijo_mayor - guardamos el valor bajamos de nivel x la izquierda
        if nodo_actual.hijo_menor is not None and nodo_actual.hijo_mayor is None:
            self.agrega_valor_desc(nodo_actual.valor)
            nodo_actual = nodo_actual.hijo_menor
            self.valor_desc(nodo_actual)
            nodo_actual = nodo
            return self.lista_valores_desc

        # nodo sin hijo menor y con hijo mayor - y bajamos de nivel por la derecha,y luego guardamos el valor del nodo
        if nodo_actual.hijo_menor is None and nodo_actual.hijo_mayor is not None:
            nodo_actual = nodo_actual.hijo_mayor
            self.valor_desc(nodo_actual)
            nodo_actual = nodo
            self.agrega_valor_desc(nodo_actual.valor)
            return self.lista_valores_desc
