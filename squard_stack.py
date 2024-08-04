#합격자 수 구하는 함수 정의
def count_passer(score, c):
    answer = 0                          #합격자 수 받을 변수 선언
    for i in score:                     #score 리스트의 원소를 반복하여 꺼냄
        if i >= c:                      #합격 커트라인보다 높을 경우
            answer += 1                 #answer 1씩 더함
    return answer
# [80, 40, 90, 55, 94, 30, 60, 44]
print(count_passer([80, 40, 90, 55, 94, 30, 60, 44], 60))
print(count_passer([20, 50, 20, 80, 45], 30))

# 스택문제 1번 ("123//45/6789///")
def backspace_string(input_string):
    stack = []                          #꺼낸 값들을 넣을 수 있는 리스트 변수 선언

    for i in input_string:              #입력한 값의 원소들을 모두 반복함
        if i == '/':                    #원소가 '/'이라면, 아래 if문으로, 아니라면 else문
            if bool(stack) == True:     #이때 stack이 비어있지 않다면(원소가 있다면)  **참고) "if stack:" 으로 표현 가능함!
                stack.pop()             #".pop()" 을 사용, stack리스트에서 마지막 원소 값을 삭제함
        else:
            stack.append(i)             #원소가 '/'가 아니라면, 입력한 원소 그대로 stack에 추가함

    return ''.join(stack)               #stack의 리스트 요소들을, string으로 합쳐서 반환해주는 join 함수 사용
                                                            #".join(리스트)"
print(backspace_string("123//45/6789///"))

#리스트 안에서 최솟값 구하기
def minimum_value(nums):
    # #풀이1
    a = sorted(nums)[0]
    return (nums.index(a))

    # 풀이2
    return (nums.index(min(nums)))                  #nums 리스트 안에서 최솟값 구하기 위해 min() 사용
                                                    #리스트 안에 원소의 위치를 구하는 ".index"를 사용하여 자릿값 도출
print(minimum_value([23, 20, 73, 98, 11, 4, 288])) # 5
print(minimum_value([33, 423, 32, 2, 56])) # 3