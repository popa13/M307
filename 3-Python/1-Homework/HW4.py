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
    ################
    #### 2.2 Question 10
    ################
    print("______ Question 10 ______")
    A = sympy.Matrix(2, 4, [3, -4, 2, -4, -3, 4, 2, 3])
    print('Augmented matrix:')
    print(sympy.latex(A))
    rrefA = A.rref()[0]
    print('RREF of A:')
    print(sympy.latex(rrefA))

    ################
    #### 2.2 Question 19
    ################
    print('______ Question 19 ______')
    A = sympy.Matrix(3, 3, [-1, 1, 0, 0, 0, 1, 1, 1, 1])
    rrefA = A.rref()[0]
    print('RREF of A')
    print(sympy.latex(rrefA))

    ####################
    #### 2.3 Question 6
    ####################
    print('_______ Question 6 ______')
    A = sympy.Matrix(3, 3, [0, 1, 1, 4, 5, -3, -1, -3, -1])
    print('Augmented Matrix:')
    print(sympy.latex(A))
    print('RREF of A:')
    print(sympy.latex(A.rref()[0]))

    ######################
    #### 2.3 Question 14
    ######################
    print('______ Question 14 ______')
    A = sympy.Matrix(3, 3, [2, 1, 1, -1, 3, -4, 0, -1, -1])
    print('Matrix A:')
    print(sympy.latex(A))
    print('RREF of Matrix A:')
    print(sympy.latex(A.rref()[0]))

    #######################
    #### 2.3 Question 26 a) and b)
    #######################
    print('______ Question 26 ______')
    print('Part a)')
    A = sympy.Matrix(4, 5, [0, 0, 1, 1, 1, 1, -1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1])
    print('Augmented Matrix of A:')
    print(sympy.latex(A))
    print('RREF of A:')
    print(sympy.latex(A.rref()[0]))