import sympy
from sympy import Function, Eq

stop = False

if __name__ == '__main__':
    while not stop:
        printExample = input(
            "Which example you want to print? Enter 1, 2, 3, or 4.\nEnter q if you want to quit.\n")
        ##################
        ### Example 1
        ##################
        if printExample != 'q' and int(printExample) == 1:
            print('______ Example 1 ______')
            A = sympy.Matrix(2, 2, [1, 2, -1, 4])
            print(A.eigenvals())
            print(A.jordan_form())

            x = sympy.symbols('x')
            M = sympy.Matrix(2, 2, [2 * sympy.exp(2*x), sympy.exp(3*x), sympy.exp(2*x), sympy.exp(3*x)])
            print(M)
            V = sympy.Matrix(2, 1, [sympy.exp(-2*x)*(2*x - 3)/4, sympy.exp(-3*x)*(3*x + 7)/9])
            print(sympy.latex(M * V))

            y1, y2 = sympy.symbols('y1 y2', cls=Function)
            x = sympy.symbols('x')

            Eq1 = Eq(y1(x).diff(), y1(x) + 2*y2(x) + 2)
            Eq2 = Eq(y2(x).diff(), -y1(x) + 4*y2(x) + x)

            system = [Eq1, Eq2]
            solution = sympy.dsolve(system, [y1(x), y2(x)])
            print(solution)
            print(str(solution[0].lhs) + ' = ' + str(solution[0].rhs))
            print(str(solution[1].lhs) + ' = ' + str(solution[1].rhs))

