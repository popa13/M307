import numpy as np
import matplotlib.pyplot as plt


def ex1DF(x, y):
    return -4*x - y, 2*x + y

stop = False

if __name__ == '__main__':
    while not stop:
        printExample = input(
            "Which example you want to print? Enter 1.\nEnter q if you want to quit.\n")
        ##################
        ### Example 1
        ##################
        ## Phase portrait
        if printExample != 'q' and int(printExample) == 1:
            print('______ Example 1 ______')
            X, Y = np.meshgrid(np.linspace(-3.0, 3.0, 30), np.linspace(-3.0, 3.0, 30))
            dX, dY = ex1DF(X, Y)

            plt.streamplot(X, Y, dX, dY, color='r', linewidth=1, density=0.8)
            plt.axis('square')
            plt.axis([-3, 3, -3, 3])
            plt.show()

            print('____________________________')




