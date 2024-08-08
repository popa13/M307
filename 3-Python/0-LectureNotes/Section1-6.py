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
    while not stop:
        #####################
        #####  Which example?
        #####################
        printExample = input("Which example do you want to print? Enter a number?\nChoose between 4 and 7.\nEnter q to quit\n")

        #####################
        ###  Example 4
        #####################
        if printExample != 'q' and int(printExample) == 4:
            print("_______ Example 4 _______")
            A = sympy.Matrix(3, 3, [-2, 3, 0, 4, 10, 2, -5, 7, 0])
            C = A.cofactor_matrix()
            print("Matrix of cofactors")
            printMatrix(C)
            printMatrix(A.inv())
            print("_________________________")

        #####################
        ###  Example 7
        #####################
        if printExample != 'q' and int(printExample) == 7:
            print("_______ Example 7 _______")
            A = sympy.Matrix(3,3, [-2, 3, 0, 4, 10, 2, -5, 7, 0])
            B = sympy.Matrix(3, 1, [2, 3, 1])
            AInv = A.inv()
            sol = AInv * B
            print("The solution is")
            print("x = " + str(sol[0]))
            print("y = " + str(sol[1]))
            print("z = " + str(sol[2]))

            A3 = sympy.Matrix(3, 3, [-2, 3, 2, 4, 10, 3, -5, 7, 1])
            print("det (A3) = " + str(A3.det()))


        ###### Do you quit?
        if printExample == 'q':
            stop = True