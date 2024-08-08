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
    print('______ Section 6.2, Problem 2 ______')
    A = sympy.Matrix(2, 2, [6, -8, 4, -6])
    JCF = A.jordan_form()
    printMatrix(JCF[0])
    printMatrix(JCF[1])