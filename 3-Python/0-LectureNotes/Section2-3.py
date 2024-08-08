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
    A = sympy.Matrix(3, 4, [1, 3, -1, 0, 2, 2, 2, 0, 3, 1, 5, 0])
    reffA = A.rref()[0]
    printMatrix(reffA)

    ####################
    ### Example 2
    ####################
    print("_______ Example 2 _______")
    A = sympy.Matrix(3, 4, [1, 1, 0, 0, 0, -1, 1, 0, 1, 1, 1, 0])
    reffA = A.rref()[0]
    printMatrix(reffA)

    ####################
    ### Example 4
    ####################
    print("_______ Example 4 _______")
    A = sympy.Matrix(3, 3, [1, 3, -1, -2, -6, 3, 3, 9, 0])
    rrefA = A.rref()[0]
    printMatrix(rrefA)

    ####################
    ### Example 5
    ####################
    print("_______ Example 5 _______")
    A = sympy.Matrix(3, 3, [1, 1, -1, 0, 1, 1, 1, 1, 1])
    rrefA = A.rref()[0]
    printMatrix(rrefA)

    ####################
    ### Example 10
    ####################
    print("_______ Example 10 _______")
    A = sympy.Matrix(3, 4, [1, 1, -3, 1, 0, 1, 1, 3, 1, 1, 1, 7])
    rrefA = A.rref()[0]
    printMatrix(rrefA)