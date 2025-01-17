import numpy as np

#Create a 4x4 matrix where the diagonal elements are 1, and the rest are 0.
print("*----Create a 4x4 matrix where the diagonal elements are 1, and the rest are 0.----*")
matrix = np.eye(4)
print(matrix)

#Create a 1D array of 15 numbers evenly spaced between 0 and 5.
print("*----Create a 1D array of 15 numbers evenly spaced between 0 and 5.----*")
arr = np.linspace(0,5,15)
print(arr)

# Create a 3x3 matrix with random integers between 10 and 50.
# Compute the sum of each row.
# Compute the product of all elements in the matrix.
print("*----Create a 3x3 matrix with random integers between 10 and 50.")
print("Compute the sum of each row.")
print("Compute the product of all elements in the matrix.----*")
random_arr = np.random.randint(10,51, size = (3,3))
print(random_arr)
# for index in random_arr:
#     print(sum(index))
#or
rows_sum = np.sum(random_arr, axis=1)
print(rows_sum)
rows_product = np.prod(random_arr)
print(rows_product)

#Normalize the 3x3 matrix so all its elements fall between 0 and 1.
