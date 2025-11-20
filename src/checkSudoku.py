# src/sudoku.py
# Combina todos los checks para validar un Sudoku completo

from .checkFilas import checkFilas
from .checkColumnas import checkColumnas
from .checkCuadrado import checkCuadrado
from .checkNumerosValidos import checkNumerosValidos

def checkSudoku(sudoku):
    return (
        checkCuadrado(sudoku)
        and checkNumerosValidos(sudoku)
        and checkFilas(sudoku)
        and checkColumnas(sudoku)
    )

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    import casosTest.casosTestSudoku as casos

    for nombre in casos.__dict__:
        if not nombre.startswith("__"):
            print(nombre, "=>", checkSudoku(casos.__dict__[nombre]))
