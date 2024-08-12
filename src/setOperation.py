from init import universe_set
#* by defining a fast enough union, everything else should have a low time complexity (except the complement)



#* o(n)
def setCasting(set1:set) -> dict:
    return {x:"_" for x in set1}

#* o(n)
#* Declarive Cycle
def union(set1:dict, set2:dict) -> set:
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
    return set({**set1, **set2}.keys())

#* o(n)
#* Declarative Cycle
def complement(set1:set) -> set:
    #TODO: Comment this shit
    return set(x for x in universe_set if x not in set1)

#* o(n)
#* Declarative Functional
def intersection(set1:set, set2:set) -> set:
    #TODO: Comment this shit
    return set(complement(union({setCasting(complement(set1))}, {setCasting(complement(set2))}))) #TODO: use the mapping function for the hashet

#* o(n)
#* Declarative Functional
def difference(set1:set, set2:set) -> set:
    #TODO: Comment this shit
    return set(intersection(set1, {setCasting(complement(set2))})) #TODO: Use the mapping function for the hashset

#* o(n+m)
#* Declarative Functional
def simetricDifference(set1:set, set2:set) -> set:
    #TODO: comment this shit
    return set(union({setCasting(difference(set1, set2))},setCasting(difference(set2, set1)))) #TODO:Use the mapping funcion for the hashset




# Debuggin purpose
# TODO: do a linear function for mapping for a hashset
set1 = {"z":"_","e":"_","1":"_","c":"_"}
set2 = {"a":"_","b":"_","c":"_", "e":"_"}

print({**set1, **set2})