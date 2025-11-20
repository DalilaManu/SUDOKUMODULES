
def checkColumnas(sudoku):
    assert isinstance(sudoku, list), "La entrada debe ser una lista"

    n = len(sudoku)

    for columna in range(n):
        numeros_vistos = []

        for fila in range(n):
            numero = sudoku[fila][columna]

            if numero in numeros_vistos:
                return False

            numeros_vistos.append(numero)

    return True



if __name__ == "__main__":
    import sys
    sys.path.append("..")

    import casosTest.casosTestSudoku as casos

    for nombre in casos.__dict__:
        if not nombre.startswith("__"):
            print(nombre, "=>", checkColumnas(casos.__dict__[nombre]))
