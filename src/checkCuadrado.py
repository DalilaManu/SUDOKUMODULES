
def checkCuadrado(sudoku):
    n = len(sudoku)
    for fila in sudoku:
        if len(fila) != n:
            return False
    return True



if __name__ == "__main__":
    import sys
    sys.path.append("..")

    import casosTest.casosTestSudoku as casos

    for nombre in casos.__dict__:
        if not nombre.startswith("__"):
            print(nombre, "=>", checkCuadrado(casos.__dict__[nombre]))
