import numpy as np

print("\n--- List vs Array ---")
print("list:", [1,2,3,4,5] * 2) #concatenation

print("1d array:", np.array([1,2,3,4,5]) * 2)  #scalar multiplication with matrix

print("\n--- Array Creation ---")
arr_1d = np.array([1,2,3,4,5])
arr_2d = np.array([[1,2,3],
                    [4,5,6]])

print("\n--- Default Value Arrays ---")
print(np.zeros((3,3))) #3x3 array of 0s
print(np.ones((2,3))) #2x3 array of 1s
print(np.full((2,2),6)) #2x2 array of 6s
print(np.eye(3)) #identity matrix
print(np.arange(1,10,2)) #like range function which returns an array

