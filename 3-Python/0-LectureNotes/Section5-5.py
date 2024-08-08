import numpy
import sympy


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

    stop = False
    while not stop:
        printExample = input(
            "Which example do you want to see? Enter a number?\nChoose between 1, 2, 3, 4. 5, 6, 7, 8, 9\nEnter q to quit\n")

        if printExample != 'q' and int(printExample) == 1:
            #### Example 1 #####
            print("______ Example 1 ______")
            A = sympy.Matrix(3, 3, [2, 0, 0, 0, 3, 0, 0, 0, 4])
            print("a)")
            print('A^5 = ')
            printMatrix(A * A * A * A * A)

            print('b)')
            print(A.eigenvals())

            print('c)')
            eigenVectors = A.eigenvects()
            for i in eigenVectors:
                print('lambda = ' + str(i[0]))
                print('Basis for E_lambda:')
                printMatrix(i[2][0])

        if printExample != 'q' and int(printExample) == 2:
            #### Example 2 #####
            print('______ Example 2 ______')
            A = sympy.Matrix(3, 3, [6, -4, -2, 1, 2, -1, 1, 0, 1])
            ### Solving the problem with the methods by hands
            print('a)')
            r = sympy.symbols('r')
            print((r * sympy.eye(3) - A).det())

            print('b)')
            rrefEV2 = (2 * sympy.eye(3) - A).rref()[0]
            printMatrix(rrefEV2)

            rrefEV3 = (3 * sympy.eye(3) - A).rref()[0]
            printMatrix(rrefEV3)

            rrefEV4 = (4 * sympy.eye(3) - A).rref()[0]
            printMatrix(rrefEV4)

            ### Solving the problem with the python functions
            print('a)')
            print("Eigenvalues:")
            print(A.eigenvals())

            print('b)')
            eigenVectors = A.eigenvects()
            for i in eigenVectors:
                print('lambda = ' + str(i[0]))
                print('Basis for E_lambda:')
                printMatrix(i[2][0])

            print('c)')
            ### Creating the matrix of eigenvectors
            P = eigenVectors[2][2][0]
            P = P.col_insert(0, eigenVectors[1][2][0])
            P = P.col_insert(0, eigenVectors[0][2][0])
            printMatrix(P)
            Pinv = P.inv()
            printMatrix(Pinv)
            D = Pinv * A * P
            print("Diagonalization of A:")
            printMatrix(D)
            print("A^5 = P D^5 Pinv = ")
            printMatrix(P * D * D * D * D * D * Pinv)
            print('A^5 directly = ')
            printMatrix(A * A * A * A * A)

        if printExample != 'q' and int(printExample) == 4:
        #### Example 4 #####
            print('______ Example 4 ______')
            A = sympy.Matrix(3, 3, [1, -2, -6, -2, 2, -5, 2, 1, 8])
            ### Calculation by hand
            r = sympy.symbols('r')
            print((r * sympy.eye(3) - A).det())
            rrefEV5 = (5 * sympy.eye(3) - A).rref()[0]
            printMatrix(rrefEV5)
            rrefEV3 = (3 * sympy.eye(3) - A).rref()[0]
            printMatrix(rrefEV3)
            ###### Calculation with Python functions
            eigenVectors = A.eigenvects()
            sum = 0
            toPrintEigenSpace = ''
            for i in eigenVectors:
                print('dim(E_{' + str(i[0]) + '}) = ' + str(len(i[2])))
                toPrintEigenSpace += ' + ' + 'dim(E_{' + str(i[0]) + '})'
                sum += len(i[2])
            if sum == 3:
                print('The matrix is diagonalization because ' + toPrintEigenSpace + ' = 3')
            else:
                print('The matrix is not diagonalizable because ' + toPrintEigenSpace + ' != 3')

        if printExample != 'q' and int(printExample) == 5:
            #### Example 5 #####
            print('______ Example 5 ______')
            A = sympy.Matrix(2, 2, [1, -1, 1, 1])
            sum = 0
            eigenVectors = A.eigenvects()
            toPrintEigenSpace = ''
            for i in eigenVectors:
                print('dim(E_{' + str(i[0]) + '}) = ' + str(len(i[2])))
                toPrintEigenSpace += ' + ' + 'dim(E_{' + str(i[0]) + '})'
                sum += len(i[2])
            if sum == 2:
                print('The matrix is diagonalization because ' + toPrintEigenSpace + ' = 2')
            else:
                print('The matrix is not diagonalizable because ' + toPrintEigenSpace + ' != 2')

            P = eigenVectors[0][2][0]
            P = P.col_insert(1, eigenVectors[1][2][0])
            printMatrix(P)
            D = P.inv() * A * P
            for i in numpy.arange(0,2, 1):
                for j in numpy.arange(0, 2, 1):
                    D[i, j] = sympy.simplify(D[i, j])
            print('Diagonalization of A = ')
            printMatrix(D)
            print("Remark: To obtain the diagonalization of a matrix\n"
                  "we simply put the eigenvalues along the main diagonal!")

        if printExample != 'q' and int(printExample) == 7:
            ##### Example 7 #####
            print('______ Example 7 ______')
            A = sympy.Matrix(3, 3, [1, -2, -6, -2, 2, -5, 2, 1, 8])
            JCF = A.jordan_form()
            print('Jordan Canonical Form = ')
            ## The second item in JCF is the Jordan Canonical Form
            printMatrix(JCF[1])
            print('The matrix P such that B = Pinv * A * P is the first item in JCF:')
            printMatrix(JCF[0])
            print("So, the Jordan Canonical Form is Pinv * A * P = ")
            printMatrix(JCF[0].inv() * A * JCF[0])

        if printExample != 'q' and int(printExample) == 39:
            print('______ Section 5.5, Exo. 39 ______')
            A = sympy.Matrix(5, 5, [21, 1, -4, -11, -4, 43, 4, -3, -22, -19, 10, 1, -1, -7, 0, 22, 1, -4, -12, -4, 22, 1, -4, -11, -5])
            printMatrix(A)
            JCF = A.jordan_form()
            print('Change of basis P = ')
            printMatrix(JCF[0])
            print('Jordan Canonical Form of A = ')
            printMatrix(JCF[1])

        #### Continue or not?
        if printExample == 'q':
            stop = True

