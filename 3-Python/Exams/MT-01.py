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
        printQuestion = input(
            "Which example do you want to see? Enter a number?\nChoose between 1, 2, 3, 4.\nEnter q to quit\n")

        #################
        ### Question 2
        #################
        if printQuestion !='q' and int(printQuestion) == 2:
            print("______ Question 2 ______")
            print('b)')
            A = sympy.Matrix(3, 3, [2, -1, 3, 1, 1, -2, 1, 1, 5])
            Ainv = A.inv()
            print('Answer:')
            printMatrix(Ainv)

            print('c)')
            B = sympy.Matrix(3, 1, [42, 42, 21])
            X = Ainv * B
            print('Answer:')
            printMatrix(X)

        ##################
        ### Question 3
        ##################
        if printQuestion != 'q' and int(printQuestion) == 3:
            print("______ Question 3 ______")
            A = sympy.Matrix(3, 3, [-3, 0, 4, 2, -1, 3, 4, 0, 5])
            B = sympy.Matrix(3, 3, [2, -1, 3, 0, 1, 0, -3, 2, 1])
            print('b)')
            print("Answer:")
            printMatrix(A * B.transpose())

            print("d)")
            print('Answer:')
            printMatrix(B * A.transpose())
            print(str((B * A.transpose()).det()))

        ##################
        ### Question 4
        ##################
        if printQuestion != 'q' and int(printQuestion) == 4:
            print("______ Question 4 ______")
            A = sympy.Matrix(3, 3, [3, -1, 0, 0, 1, -3, 2, 0, 1])
            Adet = A.det()
            A1 = sympy.Matrix(3, 3, [1, -1, 0, 1, 1, -3, 1, 0, 1])
            A2 = sympy.Matrix(3, 3, [3, 1, 0, 0, 1, -3, 2, 1, 1])
            A3 = sympy.Matrix(3, 3, [3, -1, 1, 0, 1, 1, 2, 0, 1])
            print("Answer:")
            print("x = det(A1)/det(A) = " + str(A1.det() / Adet) + ', y = det(A2)/det(A) = ' + str(A2.det() / Adet) + ', z = det(A3)/det(A) = ' + str(A3.det() / Adet))

