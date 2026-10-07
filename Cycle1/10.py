arr = [[0, 0, 0, 1, 0],
       [2, 0, 0, 0, 3],
       [0, 0, 0, 4, 0]]

dict = {}

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] != 0:

            dict[i, j] = arr[i][j]

print("Position of non-zero elements in the matrix:")
print(dict)