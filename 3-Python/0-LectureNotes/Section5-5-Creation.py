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

    #### Example 2 #####
    print("______ Example 2 ______")
    P = sympy.Matrix(3, 3, [2, 2, 3, 1, 1, 1, 2, 1, 1])
    Pinv = P.inv()
    A = sympy.diag(2, 3, 4)
    B = P * A * Pinv
    printMatrix(B)

    print('')
    A = sympy.Matrix(3, 3, [6, -4, -2, 1, 2, -1, 1, 0, 1])
    k = sympy.symbols('k')
    Ak = k * sympy.eye(3) - A
    print('kI - A = ')
    printMatrix(Ak)
    print('det(kI - A) = ')
    print(Ak.det())
    print('EigenValues and EigenVectors:')
    eigenVect = A.eigenvects()
    ev1 = eigenVect[0]
    print(str(ev1[0]) + ', Dim(E_' + str(ev1[0]) + ') = ' + str(ev1[1]) + ', Basis: ')
    printMatrix(ev1[2][0])

    ev2 = eigenVect[1]
    print(str(ev2[0]) + ', Dim(E_' + str(ev2[0]) + ') = ' + str(ev2[1]) + ', Basis: ')
    printMatrix(ev2[2][0])

    ev3 = eigenVect[2]
    print(str(ev3[0]) + ', Dim(E_' + str(ev3[0]) + ') = ' + str(ev3[1]) + ', Basis: ')
    printMatrix(ev3[2][0])

    P = sympy.Matrix(3, 3, [1, 2, 3, sympy.Rational(1, 2), 1, 1, 1, 1, 1])
    Pinv = P.inv()
    D = Pinv * A * P
    print('Diagonal matrix after change of basis:')
    printMatrix(D)

    ### Example 7
    print("_____ Example 7 _____")
    A = sympy.Matrix(3, 3, [1, -2, -6, -2, 2, -5, 2, 1, 8])
    eigenStuff = A.eigenvects()
    i = 1
    for eigen in eigenStuff:
        print(str(i) + ") Eigen Value: " + str(eigen[0]))
        print('Multiplicity (dimension of eigenspace): ' + str(eigen[1]))
        print('EigenVector: ')
        printMatrix(eigen[2][0])
        i+=1

    print("Eigen vector for 3")
    B = sympy.diag(3, 3, 3) - A
    Brref = B.rref()[0]
    print('Solution to (lambda I - A) = 0:')
    printMatrix(Brref)
    B = B * B
    print('Solution to (lambda I - A)^2 = 0:')
    Brref = B.rref()[0]
    printMatrix(Brref)
    B = B * B
    print('Solution to (lambda I - A)^3 = 0')
    Brref = B.rref()[0]
    printMatrix(Brref)
    P = sympy.Matrix(3, 3, [-2, 0, -1, -1, 1, -1, 1, 0, 1])
    JF = P.inv() * A * P
    print('JF = ')
    printMatrix(JF)

    print('Eigenvector for 5')
    B = sympy.diag(5, 5, 5) - A
    Brref = B.rref()[0]
    printMatrix(Brref)

    printMatrix(A * eigenStuff[0][2][0])

    print('Jordan Form')
    JordanA = A.jordan_form()
    P = JordanA[0]
    print("P = ")
    printMatrix(P)
    B = JordanA[1]
    BfromA = P.inv() * A * P
    print("B = ")
    printMatrix(B)
    print("P^{-1} A P = ")
    printMatrix(BfromA)

    #### Exo 39
    A = sympy.Matrix(5, 5, [21, 1, -4, -11, -4, 43, 4, -3, -22, -19,
                            10, 1, -1, -7, 0, 22, 1, -4, -12, -4,
                            22, 1, -4, -11, -5])
    print('A = ')
    printMatrix(A)
    JordanA = A.jordan_form()
    P = JordanA[0]
    B = JordanA[1]
    print('B = ')
    printMatrix(B)