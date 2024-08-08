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
    ### Example 1
    ####################
    print("_______ Example 1 _______")
    A = sympy.Matrix(4, 4, [2, 3, -1, 0, -1, -1, 3, 0, 1, 2, 2, 0, 0, 1, 5, 0])
    rrefA = A.rref()[0]
    printMatrix(rrefA)