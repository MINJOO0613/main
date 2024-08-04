# 07.26 임우재튜터 행렬 최댓값 구하기
matrix = []
for i in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)

# print(matrix[4][6])

# def input_matrix(n):
#     matrix = []
#     for i in range(10):
#         row = list(map(int, input().split()))
#         matrix.append(row)
#     return matrix

def find_max(matrix):
    max_value = matrix[0][0]                    # -1로 수정하는 게 좋음
    max_positon = None
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value > max_value:
                max_value = value
                max_postion = i+1, j+1
    print(max_value)
    print(max_postion)
    return max_value, max_postion

max_value = -1
for i in range(9):
    max_value = max(max_value, max(matrix[i]))

find_max(matrix)