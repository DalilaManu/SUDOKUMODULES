# src/checkNumerosValidos.py
# Verifica que los números sean enteros y estén dentro del rango correcto

def checkNumerosValidos(sudoku):
    n = len(sudoku)
    for fila in sudoku:
        for num in fila:
            if not isinstance(num, int) or not (1 <= num <= n):
                return False
    return True

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    import casosTest.casosTestSudoku as casos

    for nombre in casos.__dict__:
        if not nombre.startswith("__"):
            print(nombre, "=>", checkNumerosValidos(casos.__dict__[nombre]))
