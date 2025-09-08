# def fun(name, msg):
#     print(f'{name}님, {msg}')

# # 매개변수가 있으면 개수를 맞춰서 입력값 넣기
# # 반환값이 없으므로 함수 호출만 하면 끝
# fun('둘리', '안녕하세요')

# # 함수 응용하기
# # 입력한 숫자만큼 '안녕하세요' 출력하기
# def hello(cnt):
#     # 3번 출력하기
#     for _ in range(cnt):
#         print('안녕하세요')

# # 매개변수가 있으면 입력값을 넣어서 함수를 호출
# hello(10)
# 두 개의 숫자를 입력받아,
# 첫 번째 수에서 두 번째 수까지의 합을 반환하는 함수를 작성
# def add(a, b):
#     return a + b
# num = sum(range(5, 11))
# print(num)

# 두개의 숫자를 입력받아,
# 첫 번째 수에서 두 번째 수를 뺀 결과를 반환
# 예) 20, 10 -> 10

# 함수 이름: 내 마음대로 fun sub 등
# 입력값: 숫자 두개
# 반환값: 첫 번째 수에서 두 번째 수를 뺀 결과
# def sub(a, b):
#     return a - b
# result1 = sub(20, 10)
# print(f'결과:{result1}')
# result2 = sub(10, 20)
# print(f'잘못된 결과:{result2}')

#  def sub(n1, n2):
#          if n1 < n2:
#          return -999
#      else:
#         return 0

# a = 10 # 전역 변수

# if a%2 == 0:
#     b = 5 # 지역 변수
#     print(a, b)
# print(a, b)

# for n in range(10):
#     print(n) # 지역 변수

# def fun(x, y):
#     print(x, y) # 지역 변수

# fun(2,3)
# print(x, y) 
# 함수 블록 안에서 선언된 x,y는 지역변수로
# 함수 밖에서는 사용할 수 없다

# 숫자를 입력 받아 짝수인지 홀수인지 알려주는 함수를 만드세요

# 값을 하나 입력 받아 타입이 문자열이면 
# '문자입니다'를 출력하는 함수를 만드세요
# 타입이 str이 아니면 아무것도 출력되지 않습니다


# st = 'abc'
# def stri(st):
#      if type(st) == stri:
#          print('문자입니다')
# print(st)         

# # 값을 하나 입력 받아 0보다 크면
# # "양수입니다"를 출력하는 함수를 만드세요
# def num(n):
#     if num > 0:
#         print('양수입니다')
# n = 10
# print(num)

# 리스트를 입력받아 첫번째 값을 반환하는 함수를 만드세요

# 문자열을 입력받아 길이를 반환하는 함수를 만드세요

# 아래 코드에서 각 변수에 무엇이 저장되는지 주석을 작성
# 리스트를 입력받아 첫번째 값을 반환하는 함수 만들기
# def func(lis): # lis: 함수의 매개변수로, 함수 내부에 선언됨
#     return lis[0]
# # my_lis: 함수에 전달하기 위한 리스트로, 메인에 선언됨
# my_lis = [10, 20, 30]
# # result: 함수의 결과를 저장하기 위한 변수로, 메인에 선언됨
# result = func(my_lis)
# print(result)

# def func(msg): # msg: 함수의 매개변수로, 함수 내부에 선언됨
#     return len(msg)
# # my_str1: func 함수를 호출할 때 입력할 문자열
# my_str1 = 'abc'
# # result1: func 함수의 결과. 'abc'의 길이를 저장 할 변수
# result = func(my_str1)

# 숫자를 입력받아 양수/음수/0을 판별하는 함수를 만드세요
# 함수 정의
# 조건이 여러가지면 -> if~elif~else
# def func(num):
#     if num > 0: 
#         print('양수')
#     elif num < 0:
#         print('음수')
#     else:
#         print('0')

# # 함수 호출
# func(5) # 예상결과: '양수'
# func(-3) # 예상결과: '음수'
# func(0) # 예상결과: '0'

# 리스트를 입력받아 리스트 안의 숫자 합을 반환하는 함수

# 함수 정의
# 함수 이름, 입력값, 반환값
# 매개변수(입력값)의 이름은 자유롭게, 개수는 문제에 맞게
# def func(lis):
#     hap = 0
#     for n in lis: 
#         hap = hap + n
#     return hap
# result1 = func([1,2,3,4,5]) # 예상 결과 : 15
# print(result1)
# result2 = func([10,20,30]) # 예상 결과 : 60
# print(result2)

# # 함수이름, 매개변수 , 반환값
# # 매개변수 이름은 자유롭게, 개수는 문제에 맞게
# # 예) a b c dan num
# def func(dan):
#     for n in range(1, 10):
#         print(f'{dan} x {n} = {dan*n}')
# for i in range(2, 10):
#     print(i)
#     func(i)

# 리스트를 입력받아 그 안에
# 문자열(str) 자료형이 몇 개인지 세는 함수를 만드세요

def func(lis):
    # 전달받은 리스트에서 문자 개수 세기
    # 각 요소가 문자인지 확인
    # 리스트 안에 있는 요소 하나씩 꺼내기
    for item in lis:
        # 각 요소가 문자인지 확인
        if type(item) == str:
            print(item)

func([1, "apple", 3.5, "banana", 10, "hi"])
func(["a", "b", "c"])
func([1, 2, 3])
    