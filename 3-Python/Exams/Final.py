import sympy
import numpy


def printMatrix(arr):
    toPrint = ' '
    nbRows = arr.shape[0]
    nbCols = arr.shape[1]

    for i in numpy.arange(0, nbRows, 1):
        for j in numpy.arange(0, nbCols, 1):
            toPrint += str(arr[i, j]) + '  '
        if i < nbRows - 1:
            toPrint += '\n '
    print(toPrint)


if __name__ == '__main__':

    ######
    ## Question 2
    ######
    print('______ Question 2 ______')
    A = sympy.Matrix(3, 3, [2, 0, 1, 1, 1, 1, 0, 0, 1])
    print(A.eigenvals())
    print(A.jordan_form())

    print('______ Question 3 ______')
    A = sympy.Matrix(2, 2, [0, -1, 9, 0])
    JCF = A.jordan_form()
    print(JCF[0])
    print(JCF[1])
    P = sympy.Matrix(2, 2, [sympy.I/3, -sympy.I/3, 1, 1])
    D = sympy.Matrix(2, 2, [3*sympy.I , 0, 0, -3*sympy.I])
    printMatrix(P * D * P.inv())

    print('_____ Question 4 ______')
    A = sympy.Matrix(2, 2, [2, 1, -3, -2])
    print(A.eigenvals())
    print(sympy.latex(A))
    JCF = A.jordan_form()
    printMatrix(JCF[0])
    printMatrix(JCF[1])