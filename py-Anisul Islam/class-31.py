# use of matrix

from cairo import Matrix


# matrix = [
#     # 0 number row
#     [1, 2, 3], 
#     # 1 number row
#     [4, 5,6],
#     # 2 number row
#     [7, 8, 9],
# ]
# print(matrix[0][2])
# print(matrix[1][2])
# # // value changing
# matrix[2][2] = 10
# print(matrix[2][2])



# 
Matrix = [
    [1, 2, 3],
    [4, 5,6],
]
for row in Matrix:
    for col in row:
        print(col)