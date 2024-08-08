import sympy

if __name__ == '__main__':
    #####################
    ##### Exercise 2
    print("________ Exercise 2 ________")
    A = sympy.Matrix(3, 4, [2, 1, -2, 0, 2, -1, -2, 0, 1, 2, -4, 0])
    print(sympy.latex(A))

    e = sympy.Matrix(3, 3, [1, 0, 0, 1, -1, 0, 1, 0, -2])

    A =  e * A
    print(sympy.latex(A))

    e = sympy.Matrix(3, 3, [2, -1, 0, 0, 1, 0, 0, 3, 2])
    A = e * A
    print(sympy.latex(A))

    e = sympy.Matrix(3, 3, [3, 0, 1, 0, 1, 0, 0, 0, 1])
    A = e * A
    print(sympy.latex(A))

    ##########################
    #####  Exercise 4
    print("________ Exercise 4 ________")
    A = sympy.Matrix(3, 4, [3, 1, -2, 3, 1, -8, -14, -14, 1, 2, 1, 2])
    print(sympy.latex(A))

    e = sympy.Matrix(3, 3, [1, 0, 0, 1, -3, 0, 1, 0, -3])
    A = e * A
    print(sympy.latex(A))

    e = sympy.Matrix(3, 3, [25, -1, 0, 0, 1, 0, 0, 1, 5])
    A = e * A
    print(sympy.latex(A))

    e = sympy.Matrix(3, 3, [3, 0, 18, 0, 3, -8, 0, 0, 1])
    A = e * A
    print(sympy.latex(A))

    e = sympy.Matrix(3, 3, [1/225, 0, 0, 0, 1/75, 0, 0, 0, 1/15])
    A = e * A
    print(sympy.latex(A))

    #####  Exercise 6
    print("________ Exercise 6 ________")
    A = sympy.Matrix(3, 4, [2, 3, 1, 4, 1, 9, -4, 2, 1, -1, 2, 3])
    print(sympy.latex(A))

    e = sympy.Matrix(3, 3, [1, 0, 0, 1, -2, 0, 1, 0, -2])
    A = e * A
    print(sympy.latex(A))

    e = sympy.Matrix(3,3,[5, 1, 0, 0, 1, 0, 0, 1, 3])
    A = e * A
    print(sympy.latex(A))

    #####  Exercise 18
    print("________ Exercise 18 ________")
    a, b, c = sympy.symbols('a b c')
    A = sympy.Matrix(3, 4, [1, 2, -1, a, 1, 1, -2, b, 2, 1, -3, c])
    print(sympy.latex(A))

    e = sympy.Matrix(3, 3, [1, 0, 0, 1, -1, 0, 2, 0, -1])
    A = e * A
    print(sympy.latex(A))

    e = sympy.Matrix(3, 3, [1, 0, 0, 0, 1, 0, 0, -3, 1])
    A = e * A
    print(sympy.latex(A))

    e = sympy.Matrix(3, 3, [1, 0, 0, 0, 1, 0, 0, 0, -1/2])
    A = e * A
    print(sympy.latex(A))

    ###### Exercise 24
    print("________ Exercise 24 ________")
    A = sympy.Matrix(4, 4, [1, 1, 2, 0, 3, -1, -2, 0, 2, -2, -4,0, 1, 3, 6, 0])
    print(sympy.latex(A))

    e = sympy.Matrix(4,4,[1, 0, 0, 0, -3, 1, 0, 0, -2, 0, 1, 0, -1, 0, 0, 1])
    A = e * A
    print(sympy.latex(A))

    e = sympy.Matrix(4, 4, [4, 1, 0, 0, 0, 1, 0, 0, 0, -1, 1, 0, 0, 1, 0, 2])
    A = e * A
    print(sympy.latex(A))

    e = sympy.Matrix(4, 4, [0.25, 0, 0, 0, 0, -0.25, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1])
    A = e * A
    print(sympy.latex(A))


