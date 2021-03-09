import numpy as np
matrix_list = []
for i in range(5):
    array_number = input()
    list_number = array_number.split(' ')
    number = [int(number, base=10) for number in list_number]
    matrix_list.append(number)
matrix = np.array(matrix_list)
matrix = matrix.reshape(5, 5)
a, b = np.where(matrix == 1)
print(abs(a[0]-2) + abs(b[0]-2))
# import numpy as np
# array_number = input()
# list_number = array_number.split(' ')
# print(list_number)
# matrix = [int(number) for number in list_number]
# matrix = np.array(matrix)
# matrix = matrix.reshape(5, 5)
# a, b = np.where(matrix == 1)
# print(abs(a[0]-2) + abs(b[0]-2))
 