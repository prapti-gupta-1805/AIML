import numpy as np

#List vs Array
print("list:", [1,2,3,4,5] * 2) #concatenation

print("1d array:", np.array([1,2,3,4,5]) * 2)  #scalar multiplication with matrix

#Array Creation
arr_1d = np.array([1,2,3,4,5])
arr_2d = np.array([[1,2,3], [4,5,6]])

#Default Value Arrays
print(np.empty((2,2))) #2x2 array with uninitialized values
print(np.zeros((2,2))) #3x3 array of 0s
print(np.ones((2,2))) #3x3 array of 1s
print(np.full((2,2),6)) #2x2 array of 6s
print(np.eye(2)) #identity matrix
print(np.arange(1,10,2)) #like range function but returns an array - [1 3 5 7 9]
print(np.linspace(0,1,5)) #5 evenly spaced numbers between 0 and 1 - [0.0 0.25 0.5 0.75 1.0]