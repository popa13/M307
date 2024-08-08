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


stop = False

if __name__ == '__main__':
    ### Section 2.4, exo 14
    A = sympy.Matrix(3, 4, [0, 1, 2, 4, -2, -1, 0, -2, 1, 0, -1, -1])
    print(sympy.latex(A))
    print(sympy.latex(A.rref()[0]))

    a, b, c = sympy.symbols('a b c')
    A = sympy.Matrix(3, 3, [0, 1, a, -2, -1, b, 1, 0, c])
    print(sympy.latex(A))
    interchangeEq(1, 3, A)
    printMatrix(A)
    interchangeByCombination(2, 1, 1, 2, A)
    printMatrix(A)
    interchangeByCombination(3, 2, 1, 1, A)
    printMatrix(A)
    multScalar(2, -1, A)
    print(sympy.latex(A))

    ### Section 5.1, exo 20a)
    A = sympy.Matrix(3, 4, [1, 1, 0, 2, -1, 0, 1, 1, 0, 1, -1, -4])
    Arref = A.rref()[0]
    printMatrix(A.rref()[0])

    result = Arref[0,3] * sympy.Matrix(4, 1, [1, 0, -1, 0]) + Arref[1, 3] * sympy.Matrix(4, 1, [2, 1, 0, 0]) + Arref[2, 3] * sympy.Matrix(4, 1, [1, 0, 0, -1])
    print(sympy.latex(result))

    ### Section 5.1, exo 22a)
    A = sympy.Matrix(3, 4, [1, 1, 0, 1, 1, -1, 1, 0, 0, 1, 1, 0])
    Arref = A.rref()[0]
    printMatrix(Arref)

    result = Arref[0, 3] * sympy.Matrix(4, 1, [1, 0, -1, 0]) + Arref[1, 3] * sympy.Matrix(4, 1, [2, 1, 0, 0]) + Arref[
        2, 3] * sympy.Matrix(4, 1, [1, 0, 0, -1])
    print(sympy.latex(result))

    ### Section 5.1 exo 24
    print('')
    A = sympy.Matrix(3, 4, [2, 1, -1, 0, -3, 1, -4, 0, 5, 2, -5, 0])
    print(sympy.latex(A))
    rrefA = A.rref()[0]
    print(sympy.latex(rrefA))

    ### Section 5.2, exo 2
    print('')
    P = sympy.Matrix(2, 2, [2, 1, 1, 1])
    PInv = P.inv()
    Talpha = sympy.Matrix(2, 2, [5, 3, -6, -4])
    print(sympy.latex(PInv) + '\n' + sympy.latex(Talpha) + '\n' + sympy.latex(P))
    Tbeta = PInv * Talpha * P
    print(sympy.latex(PInv * Talpha * P))
    print('')

    v = sympy.Matrix(2, 1, [5,-4])
    print(sympy.latex(PInv))
    print(sympy.latex(v))
    vbeta = PInv * v
    print(sympy.latex(PInv * v))
    print('')
    print(sympy.latex(Tbeta))
    print(sympy.latex(vbeta))
    TvBeta = Tbeta * vbeta
    print(sympy.latex(TvBeta))


