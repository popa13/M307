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


if __name__ == '__main__':
    ####################
    ### Example 4
    ####################
    print("_______ Example 4 _______")
    A = sympy.Matrix(3, 5, [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0])
    rrefA = A.rref()[0]
    printMatrix(rrefA)

    A = sympy.Matrix(4, 3, [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1])
    rrefA = A.rref()[0]
    printMatrix(rrefA)