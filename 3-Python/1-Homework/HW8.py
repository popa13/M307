import sympy
import numpy

from sympy import Function, Eq


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
    print('Answers to the questions of homework 8.')
    print('')

    print('_____ Question 1 _____')
    A = sympy.Matrix(3, 3, [1, 1, 1, 1, 0, 1, 0, 2, 1])
    SOL = A.inv() * sympy.Matrix(3, 1, [1, 1, 2])
    print('The solution is ')
    printMatrix(SOL)
    print('Therefore, the answer is c).')

    print('_______________________')
    print('')

    print('______ Question 2 ______')
    A = sympy.Matrix(3, 3, [1, 1, 1, 1, 2, -1, -1, 2, 3])
    B = sympy.Matrix(3, 3, [1, 2, 1, 0, 3, 1, 1, 0, 1])
    print('The product is')
    printMatrix(A * B)
    print('Therefore, the answer is c).')

    print('_________________________')
    print('')

    print('______ Question 3 ______')
    print('The eigenvalues are')
    print(A.eigenvals())
    print('Therefore the answer is a).')

    print('_________________________')
    print('')

    print('______ Question 4 ______')
    D = sympy.Matrix(3, 3, [1, 0, 0, 0, 2, 0, 0, 0, -2])
    P = sympy.Matrix(3,3, [1, 1, 1, 2, 0, 2, 0, 2, 1])
    A = P * D * P.inv()
    print('The matrix A from the problem is')
    printMatrix(A)
    print('The change of basis P is')
    printMatrix(P)
    print('Therefore, the answer is c).')

    print('_________________________')
    print('')

    print('_____ Question 5 _____')
    x, y, z = sympy.symbols('x y z', cls=Function)
    t = sympy.symbols('t')
    Eq1 = Eq(x(t).diff(), 3*x(t) - 4*y(t) + 3*z(t))
    Eq2 = Eq(y(t).diff(), -2*x(t) + 2*y(t) + 2*z(t))
    Eq3 = Eq(z(t).diff(), -x(t) - 4*y(t) + 7*z(t))
    system = [Eq1, Eq2, Eq3]
    solution = sympy.dsolve(system, [x(t), y(t), z(t)])
    print('The solution is')
    print('y1 (t) = ' + str(solution[0]))
    print('y2 (t) = ' + str(solution[1]))
    print('y3 (t) = ' + str(solution[2]))
    print('')
    print('Therefore, the answer is b).')

    print('_________________________')
    print('')
