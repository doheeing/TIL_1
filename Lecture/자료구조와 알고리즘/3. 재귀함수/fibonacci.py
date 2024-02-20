#인자로 0 또는 양의 정수인 x 가 주어질 때, Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.

#재귀적 방법

def solution(x):
    if x == 0 :
        return 0
    elif x == 1 :
        return 1
    else :
        return solution(x-1)+solution(x-2)

#반복적 방법

def sol(x):
    if x == 0 :
        return 0
    while 