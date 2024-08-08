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
        printExample = input("Which example do you want to print? Enter a number?\nChoose between 1, 2, 3, 4, 5, 8, 9, 10.\nEnter q if you want to quit.\n")

        ##########################
        #### Example 1
        ##########################
        if printExample != 'q' and int(printExample) == 1:
            print('______Example 1_______')
            A = sympy.Matrix(1, 3, [1, 2, 3])
            print("A")
            printMatrix(A)
            print(' ' + str(A))

            A = sympy.Matrix([[1, 2, 3], [4, 5, 6]])
            print('A')
            printMatrix(A)
            print(' ' + str(A))

            print("_______________________")

        ############################
        ##### Example 2
        ############################
        if printExample != 'q' and int(printExample) == 2:
            print('______Example 2_______')
            A = sympy.Matrix([[1, 2, 3], [4, 5, 6]])
            B = sympy.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            C = sympy.Matrix([[1], [-2], [4], [0]])
            D = sympy.Matrix(1, 5, [-1, 3, 0, 0.5, math.pi])

            namespace = {'A': A, 'B': B, 'C': C, 'D': D}

            for m in 'A', 'B', 'C', 'D':
                print(f"Dimension of {m} is " + str(namespace[m].shape))

            print("_______________________")

        ###############################
        ##### Example 3
        ###############################
        if printExample != 'q' and int(printExample) == 3:
            print('______Example 3_______')
            A = sympy.Matrix(2, 2, [-1, 2, 1, 12])
            B = sympy.Matrix(2, 2, [5, 2, 1, 12])
            if A == B:
                print("A is equal to B")
            else:
                print("A is not equal to B")

            A = sympy.Matrix(2, 1, [1, 2])
            B = sympy.Matrix(1, 2, [1, 2])
            if A == B:
                print("A is equal to B")
            else:
                print("A is not equal to B")

            print("_______________________")

        #################################
        #####  Example 4
        ################################
        if printExample != 'q' and int(printExample) == 4:
            print('______Example 4_______')
            A = sympy.Matrix(3, 2, [1, 2, 3, 4, 5, 6])
            B = sympy.Matrix(3, 2, [8, 9, 10, 11, 12, 13])
            C = A + B
            print('A + B = ')
            printMatrix(C)

            print("_______________________")

        ###################################
        ##### Example 5
        #################################
        if printExample != 'q' and int(printExample) == 5:
            print('______Example 5_______')
            A = sympy.Matrix([[1, 2], [3, 4]])
            B = sympy.Matrix(2, 2, [-1, -2, 1, 2])
            C = 2 * A - B
            print('2A - B = ')
            printMatrix(C)

            print("_______________________")

        ##################################
        ##### Example 8
        ##################################
        if printExample != 'q' and int(printExample) == 8:
            print('______Example 8_______')
            A = sympy.Matrix(3, 3, [1, 2, -1, 1, -3, 1, -2, 2, 1])
            B = sympy.Matrix(3, 2, [0, 0, 1, 0, 0, 1])
            C = A * B
            print('AB =')
            printMatrix(C)

            print("_______________________")

        ##################################
        ##### Example 9
        ##################################
        if printExample != 'q' and int(printExample) == 9:
            print('______Example 9_______')
            A = sympy.Matrix(3, 3, [1, 2, 3, 2, 4, 6, -1, -2, -3])
            B = sympy.Matrix(3, 3, [0, 0, 1, 1, 0, 0, 0, 1, 0])
            C = A * B
            print('AB =')
            printMatrix(C)
            C = B * A
            print('BA =')
            printMatrix(C)

            print("_______________________")

        ###################################
        ##### Example 10
        ###################################
        if printExample != 'q' and int(printExample) == 10:
            print('______Example 10_______')
            A = numpy.array([[3, 4, -5], [5, 5, -3], [-2, -5, 0.5]])
            B = numpy.array([[1], [2], [3]])
            X = numpy.linalg.solve(A, B)
            print("x1 =" + str(X[0]) + ", x2 =" + str(X[1]) + ", x3 =" + str(X[2]))

            print("_______________________")

        #### Do you want to print other examples
        if printExample == 'q':
            stop = True

    print('End of examples')
