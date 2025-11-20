
def checkFilas(sudoku):
  
    for fila in sudoku:
        if len(fila) != len(set(fila)):
            return False
    return True
