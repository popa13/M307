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
            x, y = sympy.symbols('x y', cls=Function)
            t = sympy.symbols('t')
            Eq1 = Eq(x(t).diff(), 3*x(t) + y(t))
            Eq2 = Eq(y(t).diff(), 2*y(t))
            system = [Eq1, Eq2]
            solution = sympy.dsolve(system, [x(t), y(t)])
            print(solution[0])
            print(solution[1])

        ##################
        ### Example 2
        ##################
        if printExample != 'q' and int(printExample) == 2:
            print('______ Example 2 ______')
            A = sympy.Matrix(3, 3, [1, -2, -6, -2, 2, -5, 2, 1, 8])
            print(A.eigenvals())
            print(A.jordan_form())