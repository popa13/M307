import numpy
import sympy
from sympy import shape
import math


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
    stop = False
    while not stop:
        #####################
        #####  Which example?
        #####################
        printExample = input("Which example do you want to print? Enter a number?\nChoose between 3, 6, 7, 8, 9, and 10.\nEnter q if you want to quit.\n")

        ######################################
        ##### Example 1
        ######################################
        if printExample != 'q' and int(printExample) == 2:
            print("_________ Example 3 _________")
            A = sympy.Matrix(2, 2, [1, 2, 3, 5])
            B = sympy.Matrix(2, 2, [-5, 2, 3, -1])

            printMatrix(A * B)
            printMatrix(B * A)
            printMatrix(A.inv())

        ########################################
        ######  Example 3
        ########################################
        if printExample != 'q' and int(printExample) == 3:
            print("_________ Example 3 _________")
            A = sympy.Matrix(3, 3, [1, 0, 0, 0, 1, 2, 0, 0, 1])
            print('A')
            printMatrix(A)
            B = sympy.Matrix(3, 3, [2, 1, 3, 2, 1, 1, 4, 5, 1])
            print('B')
            printMatrix(B)
            print('A^(-1)')
            C = A.inv()
            printMatrix(C)
            print('B^(-1)')
            D = B.inv()
            printMatrix(D)
            printMatrix(A * C)

            print('Product AB')
            printMatrix(A * B)
            print('Inverse of AB')
            printMatrix((A * B).inv())
            print('Product B^(-1)A^(-1)')
            printMatrix(D * C)

            print("______________________________")

        ######################################
        #####  Example 6
        ######################################
        if printExample != 'q' and int(printExample) == 6:
            print("_________ Example 6 _________")
            A = sympy.Matrix(3, 3, [1, -2, 2, 2, -3, 1, 1, -1, -1])
            if A.det() != 0:
                print("A is invertible")
            else:
                print("A is not invertible")

            print("______________________________")

        #######################################
        #####  Example 7
        #######################################
        if printExample != 'q' and int(printExample) == 7:
            print("_________ Example 7 _________")
            B = sympy.Matrix(3, 1, [6, -12, 3])
            A = sympy.Matrix(3, 3, [2, 1, 3, 2, 1, 1, 4, 5, 1])
            if A.det() != 0:
                print("A is invertible")
            else:
                print("A is not invertible")
            print("Solution to AX = B")
            X = A.inv() * B
            printMatrix(X)

            print("______________________________")

        ########################################
        #####  Example 8
        ########################################
        if printExample != 'q' and int(printExample) == 8:
            print("_________ Example 8 _________")
            E1 = sympy.Matrix(3, 3, [0, 1, 0, 1, 0, 0, 0, 0, 1])
            E2 = sympy.Matrix(3, 3, [2, 0, 0, 0, 0, 1, 0, 1, 0])
            E3 = sympy.Matrix(3, 3, [1, 2, 0, 0, 1, 0, 0, 0, 1])

            A = sympy.Matrix(3, 3, [1, 2, 3, 1, 2, 3, 1, 2, 3])

            print('Effect of E1')
            printMatrix(E1 * A)

            print("Effect of E1 on the right multiplication.")
            printMatrix(A * E1)

            print('Effect of E2')
            printMatrix(E2 * A)

            print('Effect of E3')
            printMatrix(E3 * A)

            print("______________________________")

        ##########################################
        #####  Example 9
        ##########################################
        if printExample != 'q' and int(printExample) == 9:
            print("_________ Example 9 _________")
            print("___ Step 1 ___")
            A = sympy.Matrix(3, 3, [2, 1, 3, 2, 1, 1, 4, 5, 1])
            E11 = sympy.Matrix(3, 3, [1, 0, 0, 1, -1, 0, 0, 0, 1])
            E12 = sympy.Matrix(3, 3, [1, 0, 0, 0, 1, 0, 2, 0, -1])
            A = E12 * E11 * A
            print("Left-hand side matrix")
            printMatrix(A)

            B = sympy.eye(3, 3)
            B = E12 * E11 * B
            print("Right-hand side matrix")
            printMatrix(B)

            print("___ Step 2 ___")
            E21 = sympy.Matrix(3, 3, [1, 0, 0, 0, 0, 1, 0, 1, 0])

            A = E21 * A
            print("Left-hand side matrix")
            printMatrix(A)

            B = E21 * B
            print("Right-hand side matrix")
            printMatrix(B)

            print("___ Step 3 ___")
            E31 = sympy.Matrix(3,3, [3, 1, 0, 0, 1, 0, 0, 0, 1])

            A = E31 * A
            print("Left-hand side matrix")
            printMatrix(A)

            B = E31 * B
            print("Right-hand side matrix")
            printMatrix(B)

            print("___ Step 4 ___")
            E41 = sympy.Matrix(3,3, [1, 0, -7, 0, 1, 0, 0, 0, 1])
            E42 = sympy.Matrix(3, 3, [1, 0, 0, 0, 2, -5, 0, 0, 1])

            A = E42 * E41 * A
            print("Left-hand side matrix")
            printMatrix(A)

            B = E42 * E41 * B
            print('Right-hand side matrix')
            printMatrix(B)

            print("___ Step 5 ___")
            E51 = sympy.Matrix(3, 3, [1/6, 0, 0, 0, 1, 0, 0, 0, 1])
            E52 = sympy.Matrix(3, 3, [1, 0, 0, 0, -1/6, 0, 0, 0, 1])
            E53 = sympy.Matrix(3, 3, [1, 0, 0, 0, 1, 0, 0, 0, 1/2])

            A = E53 * E52 * E51 * A
            print("Left-hand side Matrix")
            printMatrix(A)

            B = E53 * E52 * E51 * B
            print("Right-hand side Matrix")
            printMatrix(B)

            print("______________________________")

        ##########################################
        #####  Example 10
        ##########################################
        if printExample != 'q' and int(printExample) == 10:
            print("_________ Example 10 _________")
            E1 = sympy.Matrix(3, 3, [0, 1, 0, 1, 0, 0, 0, 0, 1])
            E2 = sympy.Matrix(3, 3, [3, 0, 0, 0, 1, 0, 0, 0, 1])
            E3 = sympy.Matrix(3, 3, [3, 1, 0, 0, 1, 0, 0, 0, 1])

            print('Inverse of E1')
            printMatrix(E1.inv())

            print('Inverse of E2')
            printMatrix(E2.inv())

            print('Inverse of E3')
            printMatrix(E3.inv())

            print("______________________________")

        #####
        ### Want to continue?
        if printExample == 'q':
            stop = True

    print('End of examples.')