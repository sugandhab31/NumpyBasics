import math
from random import randint

import numpy as np

#Create a NumPy array of integers from 1 to 10.
print("*----Create a NumPy array of integers from 1 to 10.----*")
arr = np.arange(1,11)
print(arr)

#Print the shape and datatype of the array.
print("*----Print the shape and datatype of the array.----*")
print(arr.shape)
print(arr.dtype)

#Reshape the array from step 1 into a 2x5 matrix.
print("*----Reshape the array from step 1 into a 2x5 matrix.----*")
print(arr.reshape(2,5))

#Find the transpose of the reshaped array.
print("*----Find the transpose of the reshaped array.----*")
arr2 = arr.reshape(2,5)
print(arr2.transpose())

#Extract the 2nd row of the matrix.
print("*----Extract the 2nd row of the matrix.----*")
print(arr2[1])

#Extract the 1st column of the matrix.
print("*----Extract the 1st column of the matrix.----*")
print(arr2[:, 0])

#Select all elements greater than 5.
print("*----Select all elements greater than 5.----*")
matrix = arr.reshape(2,5)
greater_than_five = matrix[matrix>5]

print(greater_than_five)

#Add 5 to every element in the original array.
print("*----Add 5 to every element in the original array.----*")
print(matrix+5)

#Compute the square of each element.
print("*----Compute the square of each element.----*")
print(pow(matrix,2))

#Find the sum, mean, minimum, and maximum values of the array.
print("*----Find the sum, mean, minimum, and maximum values of the array.----*")
sum_matrix = sum(matrix)
length = len(matrix.reshape(-1))
print("Sum: ",sum_matrix)
print("Mean: ", sum_matrix/length)
print("Max: ", max(arr))
print("Min: ", min(arr))

#Create a 3x3 matrix with random integers between 1 and 20.
print("*----Create a 3x3 matrix with random integers between 1 and 20.----*")
random_arr = np.random.randint(1,21, size=(3,3))
print(random_arr)

#Replace all elements greater than 10 with the value 0.
print("*----Replace all elements greater than 10 with the value 0.----*")
random_arr[random_arr > 10] = 0
print(random_arr)

