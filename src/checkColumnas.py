# src/checkColumnas.py
# Verifica que no haya números repetidos en las columnas de un Sudoku

def checkColumnas(sudoku):
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
