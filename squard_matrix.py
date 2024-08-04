# 07.25 임우재튜터 행렬의 덧셈
n, m = map(int, input().split())
matrix_a = []
# input
for i in range(n):
    row = []
    row_input = input()
    row_input_list = row_input.split()
    row_input_int_list = list(map(int, row_input_list))
    matrix_a.append(row_input_int_list)

matrix_b = []
for i in range(n):
    row = []
    row_input = input()
    row_input_list = row_input.split()
    row_input_int_list = list(map(int, row_input_list))
    matrix_b.append(row_input_int_list)

# matrix 행렬 더하기
def add_matrix(matrix_a, matrix_b):
    """
    a[i][j] + b[i][j]
    """
    result_matrix = []

    for i in range(n):
        result_row = []
        for j in range(m):
            each_sum = matrix_a[i][j] + matrix_b[i][j]
            print(each_sum)
            # result_row.append(each_sum)
        # result_matrix.append(result_row)
    for i in range(n,3):
        print(each_sum)


rlt = add_matrix(matrix_a, matrix_b)