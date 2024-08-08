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
    #################################
    ###### Section 6.2, Question 2
    #################################
    print('______ Section 6.2, Question 2 ______')
    A = sympy.Matrix(2, 2, [6, -8, 4, -6])
    JCF = A.jordan_form()
    print('JCF of A = ')
    print(sympy.latex(JCF[1]))
    print('P = ')
    print(sympy.latex(JCF[0]))

    ##################################
    ######### Section 6.3, Question 2
    ##################################
    print('______ Section 6.3, Question 2 ______')
    A = sympy.Matrix(2, 2, [4, -4, 1, 0])
    JCF = A.jordan_form()
    print('P = ')
    printMatrix(JCF[0])
    print('P^-1 = ')
    printMatrix(JCF[0].inv())
    print('JCF of A = ')
    printMatrix(JCF[1])

    ####################################
    ########### Section 6.4, Question 2
    ####################################
    A = sympy.Matrix(2, 2, [-4, 5, -4, 4])
    JCF = A.jordan_form()
    print('P = ')
    printMatrix(JCF[0])
    print(sympy.latex(JCF[0]))
    print('JCF of A = ')
    printMatrix(JCF[1])
    print(sympy.latex(JCF[1]))

    x, c_1, c_2 = sympy.symbols('x c_1 c_2')
    Z1 = sympy.Matrix(2, 1, [sympy.exp(-2*sympy.I), 0])
    Y1 = JCF[0] * Z1
    print('Y_1(x) = ')
    print(sympy.latex(Y1))

    M = sympy.Matrix(2, 2, [sympy.cos(2*x) + sympy.sin(2*x)/2, sympy.cos(2*x)/2 - sympy.sin(2*x), sympy.cos(2*x), -sympy.sin(2*x)])
    G = sympy.Matrix(2, 1, [3 * x , 0])
    Minv = M.inv()
    print(sympy.latex(Minv))

