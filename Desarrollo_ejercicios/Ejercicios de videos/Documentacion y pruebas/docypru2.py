def comprobarMail(mail):

    """
    La función comprobarMail evalúa un mail recibido en busca de la @.
    Si tiene mas de un arroba un @ o tiene el arroba al final el correo
    es incorrecto.
    
    >>> comprobarMail('juan@cursos.es')
    True

    >>> comprobarMail('juan@@cursos.es')
    False

    >>> comprobarMail('juancursos.es@')
    False

    """

    arroba=mail.count('@')

    if(arroba!=1 or mail.rfind('@')==(len(mail)-1) or mail.find('@')==0):
        return False
    else:
        return True    


import doctest
doctest.testmod()