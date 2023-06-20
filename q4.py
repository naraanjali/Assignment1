import numpy as np

# original array
original_array = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])

# Reshape the array to 2x3
reshaped_array = np.reshape(original_array, (2, 3))

print("Original Array:")
print(original_array)
print("\nReshaped Array:")
print(reshaped_array)
