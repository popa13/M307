import numpy as np
import matplotlib.pyplot as plt
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
            A = sympy.Matrix(2, 2, [1, -3, -2, 2])
            print(A.jordan_form())
            print('_____________________________')

        ####################
        #### Example 2
        ####################
        if printExample != 'q' and int(printExample) == 2:
            print('______ Example 2 ______')
            A = sympy.Matrix(3, 3, [2, -3, -3, 2, -2, -2, -2, 1, 1])
            print(A.eigenvals())
            print(A.jordan_form())
            print('_____________________________')

        #####################
        #### Example 3
        #####################
        if printExample != 'q' and int(printExample) == 3:
            print('______ Example 3 ______')
            A = sympy.Matrix(2, 2, [1, -1, 1, 1])
            print(A.eigenvals())
            print(A.jordan_form())
            print('_____________________________')

        ######################
        #### Example 4
        ######################
        if printExample != 'q' and int(printExample) == 4:
            print('______ Example 4 ______')
            A = sympy.Matrix(3, 3, [1, 1, 1, 0, 1, -1, 0, 1, 1])
            print(A.eigenvals())
            print(A.jordan_form())

            print('Solution obtained from the sympy.dsolve.')
            ### Solve with Python directly
            y1, y2, y3 = sympy.symbols('y1 y2 y3', cls=Function)
            t = sympy.symbols('t')
            # Create the system of differential equations
            # Explicitly multiply the right-hand side AY
            # to obtain Eq1, Eq2, and Eq3
            Eq1 = Eq(y1(t).diff(), y1(t) + y2(t) + y3(t))
            Eq2 = Eq(y2(t).diff(), y2(t) - y3(t))
            Eq3 = Eq(y3(t).diff(), y2(t) + y3(t))
            system = [Eq1, Eq2, Eq3]
            # Solve the system with the method sympy.dsolve
            solution = sympy.dsolve(system, [y1(t), y2(t), y3(t)])
            # the sympy.dsolve method returns a list of equality objects
            print(solution)
            # to acces the first member of the list, type solution[0]
            # to access the left-hand side of the equality object, use solution[0].lhs
            # to access the right-hand side of the equality object, use solution[0].rhs
            print(str(solution[0].lhs) + ' = ' + str(solution[0].rhs))
            print(str(solution[1].lhs) + ' = ' + str(solution[1].rhs))
            print(str(solution[2].lhs) + ' = ' + str(solution[2].rhs))
            print('_____________________________')
