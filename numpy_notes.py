import numpy as np

#Array Creation
arr_1d = np.array([1,2,3,4,5])
arr_2d = np.array([[1,2,3], [4,5,6]])

#Default Value Arrays
print(np.zeros((2,2))) #3x3 array of 0s
print(np.ones((2,2))) #3x3 array of 1s
print(np.full((2,2),6)) #2x2 array of 6s
print(np.eye(2)) #identity matrix

print(np.arange(1,10,2)) #like range function but returns an array - [1 3 5 7 9]
print(np.linspace(0,1,5)) #5 evenly spaced numbers between 0 and 1 - [0.0 0.25 0.5 0.75 1.0]

print(np.random.random((2,2))) #2x2 array of random floats between 0 and 1

#Vector, Matrix, and Tensor
vector = np.array([1, 2, 3])
matrix = np.array([[1, 2], [3, 4]])
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

#Array Properties
print("Shape of arr_2d:", arr_2d.shape) #shape of the array
print("Data type of arr_1d:", arr_1d.dtype) #data type
print("Size of arr_2d:", arr_2d.size) #number of elements in the array
print("Number of dimensions of arr_2d:", arr_2d.ndim) #number of dimensions

#Array Reshaping
print(arr_2d.reshape((3, 2))) #reshaping to 3x2
print(arr_2d.flatten()) #flattening the 2D array to 1D - returns a copy
print(arr_2d.ravel()) #another way to flatten the array  - returns a view
print(arr_2d.T) #transpose of the array

#indexing and slicing

#on 1d array
print(arr_1d[0]) #accessing first element
print(arr_1d[1:4]) #slicing from index 1 to 4 (exclusive)

#on 2d array
print(arr_2d[0]) #accessing the second row
print(arr_2d[:, 1]) #accessing the second column
print(arr_2d[1, 2]) #accessing element at row 1, column 2

#Sorting
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(np.sort(arr)) #returns a sorted copy of the array

arr_2d = np.array([[3, 1, 4], [1, 5, 9]])
#row wise
print(np.sort(arr_2d, axis=1))
#column wise
print(np.sort(arr_2d, axis=0))

#Filtering
num = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

even = num[num % 2 == 0] #filtering even numbers

#with mask
mask = num > 5
filtered = num[mask] #filtering numbers greater than 5

#Fancy Indexing vs np.where()

indices = [0, 2, 4]
a = num[indices]  #returns elements at indices 0, 2, and 4

where = np.where(num > 5)  #returns indices where condition is true
print("Indices where num > 5:", where)  # prints the indices of elements greater than 5