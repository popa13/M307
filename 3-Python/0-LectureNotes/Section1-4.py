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
    stop = False
    while not stop:
        #####################
        #####  Which example?
        #####################
        printExample = input("Which example do you want to print? Enter a number?\nChoose between 1, 2, and 4.\nEnter q to quit\n")

        #####################
        ###  Example 1
        #####################
        if printExample != 'q' and int(printExample) == 1:
            print("_______ Example 1 _______")
            A = sympy.diag(1, 2, 3, 4, 5)
            print("The matrix A")
            printMatrix(A)
            B = sympy.diag(3, -2, 0)
            print("The matrix B")
            printMatrix(B)

            print("___________________________")

        #####################
        ###  Example 2
        #####################
        if printExample != 'q' and int(printExample) == 2:
            print("_______ Example 2 _______")
            A = sympy.diag(1, 2, -4, 3, 5)
            B = sympy.diag(-1, 2, 0, 4, 3)

            print("a) the matrix A and its inverse")
            invA = A.inv()
            print("A=")
            printMatrix(A)
            print("A^-1=")
            printMatrix(invA)

            print("b) the sum A + B.")
            if (A + B).det() != 0:
                print("The matrix A + B is invertible")
            else:
                print("The matrix A + B is not invertible")

            print("c) the product AB")
            if (A * B).det() != 0:
                print("The matrix AB is invertible")
            else:
                print("The matrix AB is not invertible")

            print("___________________________")

        #####################
        ###  Example 4
        #####################
        if printExample != 'q' and int(printExample) == 4:
            print("_______ Example 4 _______")
            A = sympy.Matrix(3, 3, [1, 2, 3, 0, 4, 5, 0, 0, 7])
            B = sympy.Matrix(3, 3, [-1, 4, 1, 0, -1, 2, 0, 0, 0])

            # 1.
            if A.det() != 0:
                print("The matrix A is invertible")
            else:
                print("The matrix A is not invertible")

            # 2.
            print(B.is_indefinite)
            if B.det() != 0:
                print("The matrix B is invertible")
            else:
                print("The matrix B is not invertible")

            # 3
            if (A * B).det() != 0:
                print("The matrix AB is invertible")
            else:
                print("The matrix AB is not invertible.")

            print("___________________________")

        ####### Do you quit?
        if printExample == 'q':
            stop = True

