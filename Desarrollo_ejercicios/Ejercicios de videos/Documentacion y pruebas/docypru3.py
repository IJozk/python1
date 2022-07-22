import math

def raizCuadrada(listaNumeros):

    """
    La funcion devuelve una lista con la raíz cuadrada de los elementos
    numericos pasados por parámetros en la otra lista
    
    >>> lista=[]
    >>> for i in [4, 9, 16]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista=[]
    >>> for i in [4, -9, 16, 60, -3]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    
    """

    return [math.sqrt(n) for n in listaNumeros]

# print(raizCuadrada([9, -16, 25, 36]))

import doctest
doctest.testmod()