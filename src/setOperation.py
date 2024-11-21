universe_set = list("abcdefghijklmnopqrstvwxyz0123456789")

#TODO: traducir la documentación, si Mario lo dice
#TODO: calcular la complejidad temporal de cada función


def nullElement(set1:dict) -> list:
    if not set1:
        return list("∅")
    else:
        return list(set1)

#* o(n)
def setCasting(set1:list) -> dict:
    """
    Realiza una comprensión de listas con valores dummy
    """
    return {x:"_" for x in set1}

#* o(n+m)
#* Ciclo Declarativo
def union(set1:dict, set2:dict) -> dict:
    """
    Dado dos diccionarios, siendo set1 y set2,
    donde los valores de cada diccionario son irrelevantes. La función union
    desempaqueta ambos diccionarios, sobrescribiendo los valores del segundo con los 
    valores del primero.

    Aquí un ejemplo bonito:

    set1 = {"z":"","e":"","1":"","c":""}
    set2 = {"a":"","b":"","c":"", "e":""}

    va a regresar 

    union = {z, e, 1, c, a, b} 

    Esta solución es o(n), porque el desempaque de por sí es lineal.

    Además de esto no utiliza funciones como tal de Python si lo queremos ver así,
    y tampoco utiliza explícitamente ninguna función.
    """
    return {**set1, **set2}

#* o(n+u)
#* Ciclo Declarativo
def complement(set1:dict) -> dict:
    """
    Dado un conjunto, que es set1, utiliza una comprensión de listas para cada valor del universo
    y verifica si el valor está en set1.
    """
    return {x:"_" for x in universe_set if x not in set1}

#* o(u^2*n*m)
#* Funcional Declarativo
def intersection(set1:dict, set2:dict) -> dict:
    """
    Dados 2 conjuntos, siendo set1 y set2, utiliza funciones de orden superior (siendo union y complement)
    para construir la operación de intersección.
    """
    return complement(union(complement(set1), complement(set2)))

#* o(u^2*n*m)
#* Funcional Declarativo
def difference(set1:dict, set2:dict) -> dict:
    """
    Dados 2 conjuntos, siendo set1 y set2, utiliza funciones de orden superior (siendo union y complement)
    para construir la operación de diferencia.
    """
    return intersection(set1, complement(set2))

#* o(u^2*n*m)
#* Funcional Declarativo
def simetricDifference(set1:dict, set2:dict) -> dict:
    """
    Dados 2 conjuntos, siendo set1 y set2, utiliza funciones de orden superior (siendo union y complement)
    para construir la operación de diferencia simétrica.
    """
    return union(difference(set1, set2),difference(set2, set1))
