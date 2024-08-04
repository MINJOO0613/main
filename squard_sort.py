# 07.24 선택정렬
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 현재 위치에서 가장 작은 요소를 찾음
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # 찾은 가장 작은 요소를 현재 위치와 교환
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)

# 삽입 정렬
def insertion_sort(arr):
    for i in range(1, len(arr)):                            #i가 두 번째 요소임
        key = arr[i]                                        #key 리스트의 원소임 (key = 83)

        j = i - 1                                           #j는 첫 번째 요소임(즉, i번째의 바로 왼쪽에 있는 원소) (j=490)
        while j >= 0 and key < arr[j]:     #key = 490, arr[j] = 44 라고 생각하고 비교 (참고로 while은 트루면 계속 돔)
            arr[j + 1] = arr[j]             # key 가 arr[j] 적다면 위치가 계속 오른쪽으로 이동함
            j -= 1                          # 역순으로 가려면 음의 수로 가야 함 그래서 -1은 계속 해야 함
        arr[j + 1] = key                    # arr[i] > arr[j] 라면, key 값이 되는거임

    return arr


if __name__ == "__main__":
    arr = [44, 490, 83, 1, 0, 34, 65, 97]
    0, 1, 34, 44, 65, 83, 97, 490
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)

# 피보나치 수열(메모이제이션)
def memo_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    # if n == 1 or n == 2:
    #     return 1

    memo[n] = memo_fibonacci(n - 1, memo) + memo_fibonacci(n - 2, memo)
    return memo[n]


print(memo_fibonacci(10))  # 55
print(memo_fibonacci(50))  # 12586269025