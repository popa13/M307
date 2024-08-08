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
        ### Example 2
        #################
        if printExample !='q' and int(printExample) == 2:
            print("______ Example 2 ______")
            print("Part 2)")
            print("Solution for T(v1)")
            A = sympy.Matrix(3, 4, [1, 1, 1, 7, 1, -1, 1, -1, 2, 1, 1, 5])
            rrefA = A.rref()[0]
            printMatrix(rrefA)

            print('')
            print('Solution for T(v2)')
            A = sympy.Matrix(3, 4, [1, 1, 1, 6, 1, -1, 1, -2, 2, 1, 1, 5])
            rrefA = A.rref()[0]
            printMatrix(rrefA)

            print('')
            print('Solution for T(v3)')
            A = sympy.Matrix(3, 4, [1, 1, 1, 6, 1, -1, 1, 2, 2, 1, 1, 5])
            rrefA = A.rref()[0]
            printMatrix(rrefA)

            print('')
            print("Part 3)")

            print("Solution for T(v1)")
            A = sympy.Matrix(3, 4, [1, 1, 1, 5, 1, -1, 1, -3, 2, 1, 1, 5])
            rrefA = A.rref()[0]
            printMatrix(rrefA)

            print("Solution for T(v2)")
            A = sympy.Matrix(3, 4, [1, 1, 1, 0, 1, -1, 1, 2, 2, 1, 1, 0])
            rrefA = A.rref()[0]
            printMatrix(rrefA)

            print("Solution for T(v3)")
            A = sympy.Matrix(3, 4, [1, 1, 1, 1, 1, -1, 1, -3, 2, 1, 1, 0])
            rrefA = A.rref()[0]
            printMatrix(rrefA)

            print("________________________")


        #################
        ### Example 3
        #################
        if printExample != 'q' and int(printExample) == 3:
            print("______ Example 3 ______")
            print("Part 1)")
            A = sympy.Matrix(3, 4, [1, 1, 1, 1, 1, -1, 1, 2, 2, 1, 1, 3])
            rrefA = A.rref()[0]
            printMatrix(rrefA)

        if printExample != 'q' and int(printExample) == 4:
            print('______ Example 4 ______')
            P = sympy.Matrix(3, 3, [1, 1, 1, 1, -1, 1, 2, 1, 1])
            Pinv = P.inv()

            print('Part 1)')
            valpha = sympy.Matrix(3, 1, [1, 2, 3])
            vBeta = Pinv * valpha
            print('[v]_beta = ')
            printMatrix(vBeta)

            print('Part 2)')
            vBeta = sympy.Matrix(3, 1, [1, 2, 3])
            vAlpha = P * vBeta
            print('[v]_alpha = ')
            printMatrix(vAlpha)

        ##################
        ### Example 5
        ##################
        if printExample != 'q' and int(printExample) == 5:
            print("______ Exapmle 5 ______")
            P = sympy.Matrix(3, 3, [1, 1, 1, 1, -1, 1, 2, 1, 1])
            Pinv = P.inv()
            vbeta = sympy.Matrix(3, 1, [1, 2, 3])
            print("P^-1 = ")
            printMatrix(Pinv)
            Talpha = sympy.Matrix(3, 3, [1, 3, -1, 2, -1, 2, 1, 3, -1])
            Tbeta = Pinv * Talpha * P * vbeta
            print("[T(v)]_beta = ")
            printMatrix(Tbeta)

        #####################
        ### Extra Example
        ####################
        if printExample != 'q' and int(printExample) == 6:
            print("______ Example 6 ______")
            A = sympy.Matrix(3, 4, [1, 1, 1, 1, 1, 2, -1, 1, 1, 0, 2, 1])
            printMatrix(A.rref()[0])

            print('')
            A = sympy.Matrix(3, 4, [1, 1, 1, -2, 1, 2, -1, 3, 1, 0, 2, 2])
            printMatrix(A.rref()[0])

            print('')
            A = sympy.Matrix(3, 4, [1, 1, 1, 0, 1, 2, -1, 1, 1, 0, 2, 1])
            printMatrix(A.rref()[0])
