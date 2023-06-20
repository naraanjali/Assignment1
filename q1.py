import numpy as np

# Creates a random vector of size 15 with integers in the range 1-20
ran_vector = np.random.randint(1, 21, size=15)

# Reshape the array to a 3 by 5 matrix
reshaped_array = ran_vector.reshape(3, 5)

print("The array shape is:", reshaped_array.shape)

# Replace the maximum value in each row with 0
reshaped_array[np.arange(3), np.argmax(reshaped_array, axis=1)] = 0

print("The Updated array is:")
print(reshaped_array)

# Create a 2-dimensional array of size 4 x 3
array_2d = np.zeros((4, 3), dtype=np.int32)

print("Array shape:", array_2d.shape)
print("Array type:", type(array_2d))
print("Array data type:", array_2d.dtype)
