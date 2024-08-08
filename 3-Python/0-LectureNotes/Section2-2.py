import numpy
import sympy

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


if __name__ == '__main__':
    ####################
    ### Example 9
    ####################
    print("_______ Example 9 _______")
    A = sympy.Matrix(3, 4, [1, 1, 0, 2, 1, 0, 1, 1, 0, -1, 1, 1])
    rrefA = A.rref()[0]
    printMatrix(rrefA)

    ####################
    ### Example 10
    ####################
    print("_______ Example 10 _______")
    A = sympy.Matrix(4, 4, [1, 1, -1, 2, -1, -2, 0, -5, 2, -1, 1, 1, 3, 2, 3, 10])
    rrefA = A.rref()[0]
    printMatrix(rrefA)

    ####################
    ### Example 11
    ####################
    print("_______ Example 11 _______")
    x, y = sympy.symbols('x y')
    A = sympy.Matrix(2, 3, [1, 2, x, -2, -4, y])
    print(A)

    interchangeByCombination(2, 1, 1, 2, A)
    print(A)
    rrefA = A.rref()[0]
    print(rrefA)

    ####################
    ### Example 12
    ####################
    print("_______ Example 12 _______")
    print("__ no 1 __")
    A = sympy.Matrix(3, 3, [1, 0, 0, 1, 1, 0, -3, -5, 3])
    rrefA = A.rref()[0]
    printMatrix(rrefA)

    print("__ no 2 __")
    A = sympy.Matrix(3, 3, [0, 0, 0, 1, 0, 1, -5, 3, 1])
    rrefA = A.rref()[0]
    printMatrix(rrefA)

    print("__ no 3 __")
    A = sympy.Matrix(4, 3, [0, 0, 0, 1, 0, 0, 1, 1, 0, -3, -5, 3])
    rrefA = A.rref()[0]
    printMatrix(rrefA)