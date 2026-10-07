import numpy as np

arr = np.arange(3 * 3 * 3).reshape(3, 3, 3)
print("Original 3D array:\n", arr)

diag_arr = np.diagonal(arr, axis1=1, axis2=2)
print("\n2D diagonal array:\n", diag_arr)