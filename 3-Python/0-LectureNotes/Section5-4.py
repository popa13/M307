import numpy
import sympy

import matplotlib.pyplot as plt


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


def printMatrixNoRound(arr):
    toPrint = ' '
    nbRows = arr.shape[0]
    nbCols = arr.shape[1]

    for i in numpy.arange(0, nbRows, 1):
        for j in numpy.arange(0, nbCols, 1):
            toPrint += str(arr[i, j]) + '  '
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

    printExample = input(
        "Which example do you want to see? Enter a number?\nChoose between 1, 4, 5, 7.\nEnter q to quit\n")

    #######
    ### Example 1
    #######
    if printExample != 'q' and int(printExample) == 1:
        print("______ Example 1 ______")
        P = sympy.Matrix(3, 3, [0.8, 0.1, 0.1, 0.03, 0.95, 0.02, 0.2, 0.05, 0.75])
        P = P.transpose()
        print(sympy.latex(P))

        printMatrix(P)
        s_0 = sympy.Matrix(3, 1, [30, 15, 55])
        print('1.')
        s_1 = P * s_0
        print('s_1 = ')
        printMatrix(s_1)
        print('2.')
        print('s_2 = ')
        s_2 = P * s_1
        printMatrix(s_2)

        print("3.")
        sValues = [s_0]
        for i in numpy.arange(1, 101, 1):
            sValues.append(P * sValues[i - 1])

        compA = numpy.zeros(101)
        compB = numpy.zeros(101)
        compC = numpy.zeros(101)
        for i in numpy.arange(0, 101, 1):
            compA[i] = sValues[i][0]
            compB[i] = sValues[i][1]
            compC[i] = sValues[i][2]
        plt.plot(numpy.arange(0, 101, 1), compA, color='b', label='Comp. A')
        plt.plot(numpy.arange(0, 101, 1), compB, color='r', label='Comp. B')
        plt.plot(numpy.arange(0, 101, 1), compC, color='g',  label='Comp. C')
        plt.legend()

        print('Steady state means: P s_N ~ s_N for large enough N.\n'
              'So 1 should be an eigenvalue for P:')
        print(P.eigenvals())
        print('Find the eigenvector:')
        ### We extract the eigenVector associated to 1
        eigenVectOne = P.eigenvects()[0][2][0]
        ### We normalize it so we have percentage
        Sum = eigenVectOne[0] + eigenVectOne[1] + eigenVectOne[2]
        eigenVectOne = (eigenVectOne / Sum) * 100
        printMatrix(eigenVectOne)

        plt.savefig('Example1-Section5-4.png')
        plt.show()

    ###########
    ### Example 4
    ###########
    if printExample != 'q' and int(printExample) == 4:
        print("______ Example 4 ______")
        A = sympy.Matrix(2, 2, [1, -3, -2, 2])

        print('Using augmented matrices (by hand).')
        print('Eigen Vector for lambda = 4:')
        rref = (4* sympy.eye(2) - A).rref()[0]
        x, y = sympy.symbols('x y')
        eigenFour = sympy.Matrix(2, 1, [-y, y])
        printMatrixNoRound(eigenFour)
        print('Remark: Infinitely many eigenvectors!')

        print('Eigenvector for lambda = -1:')
        rref = ((-1) * sympy.eye(2) - A).rref()[0]
        eigenFour = sympy.Matrix(2, 1, [3 * y / 2 , y])
        printMatrixNoRound(eigenFour)

        print('Using python commands.')
        # find the eigen values
        eigenVal = A.eigenvals()
        # A.eigenvals() returns a list with the eigenvalues and their multiplicity
        # In our example, we obtain 4 with multiplicity 1 and -1 with multiplicity
        # also 1.
        print('Eigenvalues and their multiplicities:')
        print(eigenVal)
        # Find the eigenvectors
        eigenVect = A.eigenvects()
        # A.eigenvects() return a list containing several parts:
        # each element in the list is itself a list containing the eigenvalue, the
        # multiplicity of the eigenvalue and a basis for the eigenspace
        print(eigenVect)

    ####################
    ### Example 5
    ####################
    if printExample != 'q' and int(printExample) == 5:
        print('______ Example 5 ______')
        A = sympy.Matrix(3, 3, [2, -1, 3, 0, -1, 0, 0, 0, -1])

        print('Eigen Values:')
        print(A.eigenvals())

        print('EigenVectors:')
        eigenVect = A.eigenvects()
        for i in eigenVect:
            print('lambda = ' + str(i[0]))
            print('Basis:')
            for j in numpy.arange(0, len(i[2]), 1):
                print(' ' + str(j + 1) + 'th Vector')
                printMatrix(i[2][j])

    ###############
    ### Example 7
    ###############
    if printExample != 'q' and int(printExample) == 7:
        print('______ Example 7 ______')
        A = sympy.Matrix(2, 2, [1, -1, 1, 1])
        print(A.eigenvects())

