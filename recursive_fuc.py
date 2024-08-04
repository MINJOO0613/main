def recursive_func_1(n):
    if n == 0:
        return
    else:
        recursive_func_1(n-1)
        print(n, end=' ')

recursive_func_1(5)
#먼저 f(5)가 들어가지는데, print를 만나기 전에 재귀함수를 먼저 만나기 때문에 f(4)가 반환된다.
#f(4)는 f(3)을, f(3)은 f(2)를, f(2)는 f(1)을 반환하여, 마지막 f(0)은 if문 조건에 따라 아무런 출력값 없이 종료된다.
#이때 f(1)이 가장 늦게 들어갔지만 먼저 반환되어 프린트 명령에 따라 1이 출력됨
#마찬가지로 f(2), f(3), f(4), f(5)순으로 프린트 명령으로 출력됨


#알고리즘 코드카타 39번 최대공약수 최소공배수 구하는 문제
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

#재귀함수_우재튜터님
num = int(input())
#풀이1
rlt = 1
for i in range(1, num + 1):
rlt *= i
print(rlt)

#풀이2
def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

print(fac(num))
