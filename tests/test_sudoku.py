from src.checkSudoku import checkSudoku
from casosTest.casosTestSudoku import ( correcto,
    irregular_fila,
    numero_repetido_columna,
    numero_no_presente,
    numero_fuera_del_rango,
    caracteres,
    numeros_reales,
    irregular_columna,
    lista_vacia
)

def test_sudoku_correcto():
    assert checkSudoku(correcto) == True

def test_sudoku_irregular_fila():
    assert checkSudoku(irregular_fila) == False

def test_sudoku_numero_repetido_columna():
    assert checkSudoku(numero_repetido_columna) == False

def test_sudoku_numero_no_presente():
    assert checkSudoku(numero_no_presente) == False

def test_sudoku_numero_fuera_del_rango():
    assert checkSudoku(numero_fuera_del_rango) == False

def test_sudoku_caracteres():
    assert checkSudoku(caracteres) == False

def test_sudoku_numeros_reales():
    assert checkSudoku(numeros_reales) == False

def test_sudoku_irregular_columna():
    assert checkSudoku(irregular_columna) == False

def test_sudoku_lista_vacia():
    assert checkSudoku(lista_vacia) == False


