import numpy
import sympy


def printMatrix(arr):
    toPrint = ' '
    nbRows = arr.shape[0]
    nbCols = arr.shape[1]

    for i in numpy.arange(0, nbRows, 1):
        for j in numpy.arange(0, nbCols, 1):
            toPrint += str(round(arr[i, j], 3)).zfill(3) + '  '
        if i < nbRows - 1:
            toPrint += '\n '
    print(toPrint)


if __name__ == '__main__':

    print('______ Question 1 ______')
    print('a)')
    A = sympy.Matrix(2, 4, [3, -4, 2, -4, -3, 4, 2, 3])
    Arref = A.rref()[0]
    printMatrix(Arref)
    print('b)')
    A = sympy.Matrix(3, 3, [1, 1, 2, 1, 2, 5, 2, 1, 1])
    Arref = A.rref()[0]
    printMatrix(Arref)
    print('___________________________')

    print('______ Question 2 ______')
    print('a)')
    A = sympy.Matrix(3, 3, [1, 0, 2, 3, -1, 1, -1, 2, 3])
    Arref = A.rref()[0]
    printMatrix(Arref)
    print('b)')
    Ainv = A.inv()
    valpha = Ainv * sympy.Matrix(3, 1, [1, 2, -1])
    printMatrix(valpha)
    print('__________________________')

    print('_____ Question 3 ______')
    A = sympy.Matrix(3, 3, [1, 0, 2, 3, -1, 1, -1, 2, 3])
    Ainv = A.inv()
    print('Coordinates of vs with respect to beta')
    v1beta = Ainv * sympy.Matrix(3, 1, [1, -1, 0])
    v2beta = Ainv * sympy.Matrix(3, 1, [1, 0, 1])
    v3beta = Ainv * sympy.Matrix(3, 1, [0, 1, -1])
    print(sympy.latex(v1beta))
    print('')
    print(sympy.latex(v2beta))
    print('')
    print(sympy.latex(v3beta))
    print('')

    print('Coordinates of ws with respect to alpha')
    B = sympy.Matrix(3, 3, [1, 1, 0, -1, 0, 1, 0, 1, -1])
    Binv = B.inv()
    w1alpha = Binv * sympy.Matrix(3, 1, [1, 3, -1])
    w2alpha = Binv * sympy.Matrix(3, 1, [0, -1, 2])
    w3alpha = Binv * sympy.Matrix(3, 1, [2, 1, 3])
    print(sympy.latex(w1alpha))
    print('')
    print(sympy.latex(w2alpha))
    print('')
    print(sympy.latex(w3alpha))
    print('_______________________________')

    print('______ Question 4 ______')
    P = sympy.Matrix(3,3, [1, -2, 0, 1, 3, 1, 1, 2, 1])
    Pinv = P.inv()
    print(sympy.latex(Pinv))
    print('a)')
    Talpha = sympy.Matrix(3, 3, [1, 2 ,0, 2, 0, 1, 0, 3, 4])
    Tbeta = Pinv * Talpha * P
    printMatrix(Tbeta)
    print('b)')
    valpha = sympy.Matrix(3, 1, [1, 2, 3])
    print('[v]beta = ')
    vbeta = Pinv * valpha
    printMatrix(vbeta)
    print('[T(v)]beta = ')
    printMatrix(Tbeta * vbeta)