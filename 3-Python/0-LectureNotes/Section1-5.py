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
        printExample = input("Which example do you want to print? Enter a number?\nChoose between 1, 2, 3, 4, 5, 6, 7, 8, 9.\nEnter q to quit\n")

        #####################
        ###  Example 4
        #####################
        if printExample != 'q' and int(printExample) == 4:
            print("_______ Example 4 _______")
            A = sympy.Matrix(3, 3, [2, 3, -2, -1, 6, 3, 4, -2, 1])
            Adet = A.det()
            print("det (A) = " + str(Adet))

            B = sympy.Matrix(3, 3, [1, -2, 2, 2, -3, -1, 1, -1, -1])
            Bdet = B.det()
            print("det(B) = " + str(Bdet))

            print("____________________________")

        #####################
        ###  Example 5
        #####################
        if printExample != 'q' and int(printExample) == 5:
            print("_______ Example 5 _______")
            A = sympy.Matrix(4,4, [7, -3, 0, 4, 0, 1, 0, 3, 2, 1, -2, -5, 0, 4, 0, 6])
            Adet = A.det()
            print("det(A) = " + str(Adet))

            print("__________________________")

        ####### Do you quit?
        if printExample == 'q':
            stop = True