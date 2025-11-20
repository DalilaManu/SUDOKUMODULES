# src/checkFilas.py
# Verifica que no haya números repetidos en las filas de un Sudoku

def checkFilas(sudoku):
    for fila in sudoku:
        if len(fila) != len(set(fila)):
            return False
    return True

# pruebas
if __name__ == "__main__":
    import sys
    sys.path.append("..")
    import casosTest.casosTestSudoku as casos

    for nombre in casos.__dict__:
        if not nombre.startswith("__"):
            print(nombre, "=>", checkFilas(casos.__dict__[nombre]))
