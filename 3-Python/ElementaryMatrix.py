#!/usr/bin/python3.6
# -*coding:utf-8 -*

import os
import numpy as np


def EInterchange(row1, row2):
	if (row1 == 1 and row2 == 2) or (row1 == 2 and row2 == 1):
		return np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
	elif (row1 == 1 and row2 == 3) or (row1 == 3 and row2 == 1):
		return np.array([[0, 0, 1], [0, 1, 0] , [1, 0, 0]])
	elif (row1 == 2 and row2 == 3) or (row1 == 3 and row2 == 2):
		return np.array([[1, 0, 0] , [0, 0, 1], [0, 1, 0]])
	else:
		return np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])


def EScalar(row1, scalar):
	if row1 == 1:
		return np.array([[scalar, 0, 0], [0, 1, 0], [0, 0, 1]])
	elif row1 == 2:
		return np.array([[1, 0, 0], [0, scalar, 0], [0, 0, 1]])
	else:
		return np.array([[1, 0, 0], [0, 1, 0], [0, 0, scalar]])


def ELinearComb(rowToChange, rowUsed, scalar1, scalar2):
	if rowToChange == 1 and rowUsed == 2:
		return np.array([[scalar1, scalar2, 0], [0, 1, 0], [0, 0, 1]])
	elif rowToChange == 2 and rowUsed == 1:
		return np.array([[1, 0, 0], [scalar2, scalar1, 0], [0, 0, 1]])
	elif rowToChange == 1 and rowUsed == 3:
		return np.array([[scalar1, 0, scalar2], [0, 1, 0], [0, 0, 1]])
	elif rowToChange == 3 and rowUsed == 1:
		return np.array([[1, 0, 0], [0, 1, 0], [scalar2, 0, scalar1]])
	elif rowToChange == 2 and rowUsed == 3:
		return np.array([[1, 0, 0], [0, scalar1, scalar2], [0, 0, 1]])
	elif rowToChange == 3 and rowUsed == 2:
		return np.array([[1, 0, 0], [0, 1, 0], [0, scalar2, scalar1]])
	else:
		return np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

### Test

## Change two lines
"""M = np.array([[1, 0, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0], [1,0,0,0,0,0]])

print("Initial Matrix")
print(M)
print()

i, j = 1, 1
while (i <= 3):
	j= 1
	while(j <=3):
		Level = "Row " + str(i) + " changed for row " + str(j)
		print(Level)
		print(EInterchange(i, j).dot(M))
		j+=1
	i+=1

## Scale a line
i = 1 
scalar = 2
while(i <= 3):
	Level = "Scale Row "+ str(i)
	print(Level)
	print(EScalar(i, scalar).dot(M))
	i+=1

## Change a line by a linear combinaison
i = 1
j = 1
scalar1 = 2
scalar2 = -2

while(i <= 3):
	j = 1
	while(j <= 3):
		Level = "" + str(scalar1) + "Row " + str(i) + " + " + str(scalar2) + "Row " + str(j) + " -> Row " + str(i)
		print(Level)
		print(ELinearComb(i, j, scalar1, scalar2).dot(M))
		j+=1
	i+=1 
"""