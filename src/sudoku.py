from checkFilas import checkFilas
from checkColumnas import checkColumnas
from checkCuadrado import checkCuadrado
from checkNumerosValidos import checkNumerosValidos

def checkSudoku(sudoku):
    return (
        checkCuadrado(sudoku) 
        and checkNumerosValidos(sudoku)
        and checkFilas(sudoku)
        and checkColumnas(sudoku)
    )

