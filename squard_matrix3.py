# 07.26 임우재튜터 행렬 세로 읽기
ROW_NUM = 5 # 상수
COM_MAX = 15

matrix = []
for i in range(ROW_NUM):
    row = input().strip()
    matrix.append(row)
print(matrix)

rlt = []
for pointer in range(COM_MAX):                  # pointer : 0~14
    for word in matrix:
        if pointer < len(word):                 # word : 1~15
            rlt.append(word[pointer])

print("".join(rlt))
####################################################################################
# 07.26 임우재튜터 색종이 넓이 구하기(행렬)

# 크기가 100x100인 도화지 초기화 (0으로 채워진 2차원 리스트)
canvas = [[0] * 100 for _ in range(100)]

# 색종이의 수 입력
num_papers = int(input())

# 색종이의 위치와 크기 입력 및 도화지에 표시
for _ in range(num_papers):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            canvas[i][j] = 1

# 검은 영역의 넓이 계산
black_area = sum(sum(row) for row in canvas)

# 결과 출력
print(black_area)