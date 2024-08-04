#####코드카타#####

# 알고리즘 문제 2번
def solution(num1, num2):
    if num1 < 0 or num1 > 100:      # 0 ≤ num1 ≤ 100
        return false
    if num2 < 0 or num2 > 100:      # 0 ≤ num2 ≤ 100
        return False
    return num1 * num2
print(solution(3, 4))
print(solution(27, 19))

# 알고리즘 문제 3번
def solution(num1, num2):
    if num1 < 0 or num1 > 100:      # 0 ≤ num1 ≤ 100
        return False
    if num2 < 0 or num2 > 100:      # 0 ≤ num1 ≤ 100
        return False
    return num1 // num2         #나눗셈 연산자 //를 사용하면 몫이 정수로 나옴. or int(a/b) 사용
                                #나머지를 반환하고 싶을 경우, %를 사용해야 함. ex. a % b
print(solution(10,5))
print(solution(7,2))

# 알고리즘 문제 4번
from datetime import datetime
def solution(age):
    now = datetime.now()                    # 현재 년도 구하기
    year = int(now.strftime("%Y")) + 1      # 나이는 태어난 연도에 1살이며 매년 1월 1일마다 1살씩 증가
    if age > 0 and age <= 120:              # 0 < age ≤ 120
        return year - age                   # 년도 - 나이 하여 나이 출력

print(solution(40))
print(solution(23))

# 알고리즘 문제 5번
def solution(num1, num2):
    if (num1 >= 0 and num1 <= 10000) and (num2 >= 0 and num2 <= 10000):     # 0 ≤ num1 ≤ 10,000, 0 ≤ num2 ≤ 10,000
        if num1 == num2:                        # 두 수가 같으면 1
            return "1"
        else:                                   # 두 수가 같으면 -1
            return "-1"
    return False
print(solution(2,3))
print(solution(11,11))
print(solution(7,99))

# 알고리즘 6번 문제
def solution(num1, num2):
    if num1 >= -50000 and num1 <= 50000 and num2 >= -50000 and num2 <= 50000:    #-50,000 ≤ num1 ≤ 50,000 and -50,000 ≤ num2 ≤ 50,000
        return num1 + num2                      # 두 수의 합 구하기
    return False
print(solution(2,3))
print(solution(100,2))

# 알고리즘 7번 문제
def solution(num1, num2):
    if num1 > 0 and num1 <= 100 and num2 > 0 and num2 <= 100:   # 0 < num1 ≤ 100 and 0 < num2 ≤ 100
        return int(num1 / num2 * 1000)          # num1을 num2로 나눈 값에 1,000을 곱한 후 정수로 반환
    return False
print(solution(3,2))                # 1500
print(solution(7,3))                # 2333
print(solution(1,16))               # 62

# 알고리즘 8번 문제
def solution(angle):
    angle = int(angle)                      # angle은 정수
    if angle > 0 and angle <= 180:          # 0 < angle ≤ 180
        if angle > 0 and angle < 90:         # 예각 : 0도 초과 90도 미만, 예각일 떄 "1" 반환"
           return "1"
        elif angle == 90:                   # 직각 : 90도, 직각일 떄 "2" 반환"
            return "2"
        elif angle > 90 and angle < 180:    # 둔각 : 90도 초과 180도 미만, 둔각일 떄 "3" 반환"
            return "3"
        else: return "4"                    # 평각 : 180도, 직각일 떄 "4" 반환"
    return False
print(solution(70))
print(solution(91))
print(solution(180))

# 알고리즘 9번 문제
def solution(n):
    result = 0

    if n > 0 and n <= 1000:                  # 0 < n ≤ 1000
        for i in range(n+1):                # n+1 설정해야 n까지 범위가 포함됨
            if i % 2 == 0:                  # 짝수/홀수 값 구할 때, 2로 나눈 나머지가 "0"이면 짝수, "1"이면 홀수
                result += i                 # 도출된 짝수 i의 값을 모두 더할 떄, "? += i"
        print(result)
    else:
        return False
solution(10)
solution(4)

# 알고리즘 10번 문제
def solution(numbers):
    result = []
    for number in range(1,numbers+1):
        if 0 < number <= 1000:
            result.append(number)
    return sum(result)/len(result)

print(solution(10))