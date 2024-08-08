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
    stop = False

    while (not stop):
        printExample = input(
            "Which example do you want to see? Enter a number?\nChoose between 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.\nEnter q to quit\n")

        #################
        ### Example 4
        #################
        if printExample !='q' and int(printExample) == 4:
            print("______ Example 4 ______")
            x, y, z = sympy.symbols('x y z')
            A = sympy.Matrix(3, 4, [1, 0, 1, x, 1, 1, 0, y, 0, 1, 1, z])
            Arref = A.rref()[0]
            printMatrix(Arref)

        #################
        ### Example 5
        #################
        if printExample != 'q' and int(printExample) == 5:
            print("______ Example 5 ______")
            A = sympy.Matrix(2, 4, [1, 1, -1, 0, 1, 2, 1, 0])
            rrefA = A.rref()[0]
            printMatrix(rrefA)

        #################
        ### Example 6
        #################
        if printExample != 'q' and int(printExample) == 6:
            print("______ Example 6 ______")
            A = sympy.Matrix(2, 3, [1, 1, -1, 1, 2, 1])
            rrefA = A.rref()[0]
            printMatrix(rrefA)

        #### Continue or not?
        if printExample == 'q':
            stop = True
