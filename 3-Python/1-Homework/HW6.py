import numpy
import sympy


def interchangeEq(indexEq1, indexEq2, matrix):
    indexeq1 = indexEq1 - 1
    indexeq2 = indexEq2 - 1
    temp = matrix[indexeq2, :]
    matrix[indexeq2, :] = matrix[indexeq1, :]
    matrix[indexeq1, :] = temp


def multScalar(indexEq, k, matrix):
    matrix[indexEq - 1, :] = k * matrix[indexEq - 1, :]


def interchangeByCombination(indexEq1, indexEq2, k1, k2, matrix):
    eq1Mod = k1 * matrix[indexEq1 - 1, :]
    eq2Mod = k2 * matrix[indexEq2 - 1, :]
    matrix[indexEq1 - 1, :] = eq1Mod + eq2Mod


def printMatrix(arr):
    toPrint = ' '
    nbRows = arr.shape[0]
    nbCols = arr.shape[1]

    for i in numpy.arange(0, nbRows, 1):
        for j in numpy.arange(0, nbCols, 1):
            toPrint += str(arr[i, j]).zfill(3) + '  '
        if i < nbRows - 1:
            toPrint += '\n '
    print(toPrint)


if __name__ == '__main__':
    ######################
    #### 5.4: 10
    ######################
    r = sympy.symbols('r')
    A = sympy.Matrix(3, 3, [-6, 0, -8, -4, 2, -4, 4, 0, 6])
    print(sympy.latex((r*sympy.eye(3) - A).det()))
    print((r*sympy.eye(3) - A).det().factor())

    ######################
    #### 5.4: 16
    ######################
    B = sympy.Matrix(2, 3, [2*sympy.I + 4, -5, 0, 4, 2*sympy.I - 4, 0])
    interchangeByCombination(2, 1, 2*sympy.I + 4, -4, B)
    print(sympy.latex(sympy.simplify(B)))

    #######################
    #### 5.5: 10
    #######################
    P = sympy.Matrix(3, 3, [0, -1, -1, 1, 0, 2, 0, 1, 2])
    print(sympy.latex(P.inv()))

    ########################
    #### 5.5: 16
    ########################
    P = sympy.Matrix(2, 2, [5, 5, 4 + 2*sympy.I, 4 - 2*sympy.I])
    print(sympy.latex(P.inv()))