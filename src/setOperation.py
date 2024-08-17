#* by defining a fast enough union, everything else should have a low time complexity (except the complement)


universe_set = list("abcdefghijklmnopqrstvwxyz0123456789")

#TODO: translate documentation, if mario says so
#TODO: calculate each time complexity

def nullElement(set1:dict) -> set:
    if not set1:
        return set("∅")
    else:
        return set(set1)

#* o(n)
def setCasting(set1:set) -> dict:
    """
    does list comprehension with dummy values
    """
    return {x:"_" for x in set1}

#* o(n+m)
#* Declarive Cycle
def union(set1:dict, set2:dict) -> dict:
    """
    given to dictionaries, being set1 and set2 (lmao, not appropiate names for them),
    where the values of each of the dictionaries is irrelevant. The function union 
    unpacks both dicts, while overwriting the values of the second one with the 
    values of the first one

    Aqui un ejemplo bonito:

    set1 = {"z":"_","e":"_","1":"_","c":"_"}
    set2 = {"a":"_","b":"_","c":"_", "e":"_"}

    va a regresar 

    union = {z, e, 1, c, a, b} 

    Esta solucion es o(n), porque el desempaque de por si es lineal

    Ademas de esto no utiliza funciones como tal de python si lo queremos ver asi,
    ademas de eso no utiliza explicitimante ninguna funcion 
    """
    return {**set1, **set2}

#* o(n+u)
#* Declarative Cyclic
def complement(set1:dict) -> dict:
    """
    given a set, which is set1, it uses list comprehension for each value of the universe
    and it checks if the value is in the set1
    """
    return {x:"_" for x in universe_set if x not in set1}

#* o(u^2*n*m)
#* Declarative Functional
def intersection(set1:dict, set2:dict) -> dict:
    """
    given 2 sets, being set1 and set2, it uses higher order functions (being union and complement)
    to build the set operation of intersection
    """
    return complement(union(complement(set1), complement(set2)))

#* o(u^2*n*m)
#* Declarative Functional
def difference(set1:dict, set2:dict) -> dict:
    """
    given 2 sets, being set1 and set2, it uses higher order functions (being union and complement)
    to build the set operation of difference
    """
    return intersection(set1, complement(set2))

#* o(u^2*n*m)
#* Declarative Functional
def simetricDifference(set1:dict, set2:dict) -> dict:
    """
    given 2 sets, being set1 and set2, it uses higher order functions (being union and complement)
    to build the set operation of simetricDifference
    """
    return union(difference(set1, set2),difference(set2, set1))

#! alv, que mamon esta el codigo ngl, estoy muy orgulloso de esto
#! nvm, no estoy orgulloso de el, es lento y las ultimas tres no se entienden y cuesta leerlas
