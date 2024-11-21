import src.setOperation as op

def operateSets(sets:list[dict[str,str]]):
    while True:
        print("1. Complemento")
        print("2. Union")
        print("3. Interseccion")
        print("4. Diferencia")
        print("5. Diferencia Simetrica")

        opcion = int(input("Elige una opcion: "))
        match opcion:
            case 1:
                print(f"el complemento del conjunto 1 es: {op.nullElement(op.complement(sets[0]))}")
                print(f"el complemento del conjunto 2 es: {op.nullElement(op.complement(sets[1]))}")
            case 2:
                print(f"la union de los conjuntos es: {op.nullElement(op.union(sets[0], sets[1]))}")
            case 3:
                print(f"la interseccion de los conjuntos es: {op.nullElement(op.intersection(sets[0], sets[1]))}")
            case 4:
                print(f"la diferencia de los conjuntos es: {op.nullElement(op.difference(sets[0],sets[1]))}")
            case 5:
                print(f"la diferencia simetrica de los conjuntos es: {op.nullElement(op.simetricDifference(sets[0],sets[1]))}")


def createSets() -> list[dict[str,str]]:
    set1 = None
    set2 = None

    while True:
        set1_elements = input("Entrar elementos del primero conjunto (separado por espacios): ").split()
        if all(element in op.universe_set for element in set1_elements):
            set1 = set1_elements
            break
        else: 
            print("No se ingresaron elementos válidos")

    while True:
        set2_elements = input("Entrar elementos del segundo conjunto (separado por espacios): ").split()
        if all(element in op.universe_set for element in set2_elements):
            set2 = set2_elements
            break
        else:
            print("No se ingresaron elementos válidos")
    sets = [op.setCasting(set1), op.setCasting(set2)]

    return sets

if __name__ == "__main__":
    sets = None

    while True:
        print("1. Construir Conjuntos")
        print("2. Operar conjuntos")
        print("3. Finalizar")

        opcion = int(input("Elige una opcion: "))
        if opcion >= 1 and opcion <= 3:

            match opcion:
                case 1:
                    sets = createSets()
                case 2:
                    if sets is not None:
                        operateSets(sets)
                    else:
                        print("No esta creado el conjunto")
                case 3:
                    break
