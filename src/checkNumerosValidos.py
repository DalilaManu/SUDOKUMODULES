
def sonEnteros(sudoku):
    for fila in sudoku:
        for numero in fila:
            if not isinstance(numero, int):
                return False
    return True


def estanEnRango(sudoku):
    n = len(sudoku)
    rango_valido = range(1, n+1)

    for fila in sudoku:
        for numero in fila:
            if numero not in rango_valido:
                return False
    return True


def checkNumerosValidos(sudoku):
    return sonEnteros(sudoku) and estanEnRango(sudoku)


if __name__ == "__main__":
    import sys
    sys.path.append("..")

    import casosTest.casosTestSudoku as casos

    for nombre in casos.__dict__:
        if not nombre.startswith("__"):
            print(nombre, "=>", checkNumerosValidos(casos.__dict__[nombre]))

