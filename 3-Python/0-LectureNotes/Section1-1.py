import numpy
from numpy import mgrid, cos, pi, sin
import sympy

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from mayavi import mlab


def interchangeEq(indexEq1, indexEq2, matrix):
    indexeq1 = indexEq1 - 1
    indexeq2 = indexEq2 - 1
    temp = matrix[indexeq2, :]
    matrix[indexeq2, :] = matrix[indexeq1, :]
    matrix[indexeq1, :] = temp


def multScalar(indexEq, k, matrix):
    matrix[indexEq - 1, :] = k * matrix[indexEq - 1, :]


def interchangeByCombination(indexEq1, indexEq2, k1, k2, matrix):
    eq1Mod = k1 * matrix[indexEq1 - 1, :]
    eq2Mod = k2 * matrix[indexEq2 - 1, :]
    matrix[indexEq1 - 1, :] = eq1Mod + eq2Mod


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

        #########################
        ##### Example 3:
        #########################
        print("________ Example 3 _________")
        printStep = input("Which step do you want to print? Enter a number?\nChoose between the following options\n 1. Print step 1.\n 2. Print steps 1 and 2.\n 3. Print steps 1, 2, and 3\n"
                              " 4. Plot the solution and the planes.\nEnter q if you want to quit.\n")

        #### Step 1
        if printStep != 'q' and int(printStep) == 1:
            # Augmented matrix
            m = sympy.Matrix([[2, 3, -1, 3], [-1, -1, 3, 0], [1, 2, 2, 3], [0, 1, 5, 3]])

            # First operations to get rid of the x's
            print("___ Step 1 ___")
            print("L1 + 2L2 -> L2")
            interchangeByCombination(2, 1, 2, 1, m)
            print("L1 - 2L3 -> L3")
            interchangeByCombination(3, 1, -2, 1, m)
            printMatrix(m)

        #######
        # Second operations to get rid of the y
        if printStep != 'q' and int(printStep) == 2:
            # Augmented matrix
            m = sympy.Matrix([[2, 3, -1, 3], [-1, -1, 3, 0], [1, 2, 2, 3], [0, 1, 5, 3]])

            # First operations to get rid of the x's
            print("___ Step 1 ___")
            print("L1 + 2L2 -> L2")
            interchangeByCombination(2, 1, 2, 1, m)
            print("L1 - 2L3 -> L3")
            interchangeByCombination(3, 1, -2, 1, m)
            printMatrix(m)

            print("___ Step 2 ___")
            print("3L2 - L1 -> L1")
            interchangeByCombination(1, 2, -1, 3, m)
            print("L2 + L3 -> L3")
            interchangeByCombination(3, 2, 1, 1, m)
            print("L2 - L4 -> L4")
            interchangeByCombination(4, 2, -1, 1, m)
            printMatrix(m)
            print("Notice the two lines of zeros!")

        ##### Step 3
        # Third operations to obtain 1 on the diagonal
        if printStep != 'q' and int(printStep) == 3:
            # Augmented matrix
            m = sympy.Matrix([[2, 3, -1, 3], [-1, -1, 3, 0], [1, 2, 2, 3], [0, 1, 5, 3]])

            # First operations to get rid of the x's
            print("___ Step 1 ___")
            print("L1 + 2L2 -> L2")
            interchangeByCombination(2, 1, 2, 1, m)
            print("L1 - 2L3 -> L3")
            interchangeByCombination(3, 1, -2, 1, m)
            printMatrix(m)

            print("___ Step 2 ___")
            print("3L2 - L1 -> L1")
            interchangeByCombination(1, 2, -1, 3, m)
            print("L2 + L3 -> L3")
            interchangeByCombination(3, 2, 1, 1, m)
            print("L2 - L4 -> L4")
            interchangeByCombination(4, 2, -1, 1, m)
            printMatrix(m)
            print("Notice the two lines of zeros!")

            print("___ Step 3 ___")
            print("(-1/2)L1 -> L1")
            multScalar(1, -0.5, m)
            printMatrix(m)

            print("General solution:")
            print("""x = -3 + 8z\ny= 3 - 5z""")
            print("The variable z is a free parameter.")

            print("_______________________________________")

        # Print the general solution
        if printStep != 'q' and int(printStep) == 4:
            print("_______________________________________")
            print("Plotting the solutions and the planes.")
            m = sympy.Matrix([[2, 3, -1, 3], [-1, -1, 3, 0], [1, 2, 2, 3], [0, 1, 5, 3]])

            def plane1(x, y):
                return 3 / -1.0 - 2 * x / -1.0 - 3 * y / -1.0


            def plane2(x, y):
                return x / 3.0 + y / 3.0


            def plane3(x, y):
                return -x / 2.0 - 2 * y / 2.0 + 3.0 / 2


            def plane4(x, y):
                return -y / 5.0 + 3 / 5.0


            ### Plot with mayavi
            dx, dy = 1, 1
            xGrid, yGrid = mgrid[-10:10:dx, -10:10:dy]

            # Set of solutions
            z = numpy.linspace(-5, 5, 20)
            xsol = -3 + 8 * z
            ysol = 3 - 5 * z

            # View it.
            mlab.surf(xGrid, yGrid, plane1, color=(1, 0, 0))
            mlab.surf(xGrid, yGrid, plane2, color=(1, 1, 0))
            mlab.surf(xGrid, yGrid, plane3, color=(1, 1, 1))
            mlab.surf(xGrid, yGrid, plane4, color=(1, 0, 1))
            mlab.plot3d(xsol, ysol, z, color=(0, 0, 0), line_width=00.0)
            mlab.show()

            print("_______________________________________")

        if printStep != 'q' and int(printStep) == 5:
            m = sympy.Matrix(4, 5, [1, 1, -1, 2, 1, 1, 1, -1, -1, -1, 1, 2, 1, 2, -1, 2, 2, 1, 1, 2])
            printMatrix(m)

            print('Step 1')
            interchangeByCombination(2, 1, -1, 1, m)
            interchangeByCombination(3, 1, 1, -1, m)
            interchangeByCombination(4, 1, 1, -2, m)
            printMatrix(m)

            print("Step 2")
            interchangeEq(2, 3, m)
            printMatrix(m)


        #### Continue or not?
        if printStep == 'q':
            stop = True

    print('You quit.')
