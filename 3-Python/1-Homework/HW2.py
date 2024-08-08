import sympy
import numpy


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
    #####################
    ######   Section 1.2
    #####################
    B = sympy.Matrix(3, 2, [2, -1, -3, -2, 0, 4])
    print(sympy.latex(B))
    E = sympy.Matrix(3, 3, [1, -3, 5, 2, 1, -1, 1, 1, 0])
    F = sympy.Matrix(3, 3, [1, -1, 4, 2, -3, 6, 1, 0, 1])
    print("E = " + sympy.latex(E))
    print('F = ' + sympy.latex(F))

    ### Prob 3
    print('________ Section 1.2 Prob 3 ________')
    no3 = 2 * B
    print(sympy.latex(no3))

    ### Prob 9
    print('________ Section 1.2 Prob 9 ________')
    print('E F_1 = ' + sympy.latex(E) + sympy.latex(F.col(0)))
    print(sympy.latex(E * F.col(0)))
    print('E F_2 = ' + sympy.latex(E) + sympy.latex(F.col(1)))
    print(sympy.latex(E * F.col(1)))
    print('E F_3 = ' + sympy.latex(E) + sympy.latex(F.col(2)))
    print(sympy.latex(E * F.col(2)))
    ETimesF = E * F
    print(sympy.latex(ETimesF))

    ### Prob 23
    print('________ Section 1.2 Prob 23 ________')
    A = sympy.Matrix(3, 3, [1, 0, 0, 0, 0, 1, 0, 1, 0])
    B = sympy.Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("A = " + sympy.latex(A))
    print("B = " + sympy.latex(B))
    print("(A + B)^2 = \left(" + sympy.latex(A) + ' + ' + sympy.latex(B) + "right)^2")
    print(sympy.latex((A + B) * (A + B)))

    print('A^2 = ' + sympy.latex(A * A))
    print('B^2 = ' + sympy.latex(B * B))
    print('2 AB = ' + sympy.latex(2 * A * B))
    print('A^2 + B^2 + 2AB = ' + sympy.latex(A * A + B * B + 2 * A * B))

    ### Prob 3
    print('________ Section 1.3 Prob 3 ________')
    A = sympy.Matrix(3, 6, [1, -2, 3, 1, 0, 0, 2, -1, 4, 0, 1, 0, 1, 1, 1, 0, 0, 1])
    printMatrix(A)
    print(sympy.latex(A))

    print('')
    E = sympy.Matrix(3, 3, [1, 0, 0, 2, -1, 0, -1, 0, 1])
    A = E * A
    printMatrix(A)
    print(sympy.latex(A))

    print('')
    E = sympy.Matrix(3, 3, [3, -2, 0, 0, 1, 0, 0, 1, 1])
    A = E * A
    printMatrix(A)
    print(sympy.latex(A))

    ### Prob 5
    print('________ Section 1.3 Prob 5 ________')
    A = sympy.Matrix(3, 6, [0, -2, 1, 1, 0, 0, 2, 4, -1, 0, 1, 0, 2, 1, 2, 0, 0, 1])
    printMatrix(A)
    print(sympy.latex(A))

    print('')
    E = sympy.Matrix(3, 3, [0, 0, 1, 0, 1, -1, 1, 0, 0])
    A = E * A
    printMatrix(A)
    print(sympy.latex(A))

    print('')
    E = sympy.Matrix(3, 3, [3, -1, 0, 0, 1, 0, 0, 2, 3])
    A = E * A
    printMatrix(A)
    print(sympy.latex(A))

    print('')
    E = sympy.Matrix(3, 3, [1, 0, 3, 0, 1, -1, 0, 0, 1])
    A = E * A
    printMatrix(A)
    print(sympy.latex(A))

    print('')
    E = sympy.Matrix(3, 3, [1/6, 0, 0, 0, 1/3, 0, 0, 0, -1/3])
    A = E * A
    printMatrix(A)
    print(sympy.latex(A))

    ### Prob 16
    print('________ Section 1.3 Prob 16 ________')
    a11, a12, a13, a1n, a21, a22, a23, a2n, a31, a32, a33, a3n, an1, an2, an3, ann = sympy.symbols('a_{11} a_{12} a_{13} a_{1n} a_{21} a_{22} a_{23} a_{2n} a_{31} a_{32} a_{33} a_{3n} a_{n1} a_{n2} a_{n3} a_{nn}')
    A = sympy.Matrix(4, 8, [a11, a12, a13, a1n, 1, 0, 0, 0, a21, a22, a23, a2n, 0, 1, 0, 0,
                            a31, a32, a33, a3n, 0, 0, 1, 0, an1, an2, an3, ann, 0, 0, 0, 1])
    print(sympy.latex(A))
