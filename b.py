# 함수 만들기

# 더하기 함수 정의
# 2. 입력값(매개변수) => 함수를 설계한다
# 더하기를 하기 위해 두 수를 입력
# 입력값 있고, 반환값도 있는 함수
# def add(n1, n2):
#     # 3. 결과를 만들기 위한 코드를 작성하고
#     # 결과를 리턴 또는 출력
#     # => 입력받은 두 수를 더하고 합계를 리턴
#     return n1 + n2

# # 함수 사용하기(호출하기)
# # 사용 방법
# # 함수 이름(필요한 값 입력)
# # 반환값이 있으면
# # 결과를 받고 확인해야함
# result = add(3, 4)
# print('두 수의 합:', result)
# # 또는

# # 함수 만들기
# def func1(a):
#     print(a)

# # 함수 호출하기
# func1(1)

# # 값을 두개 입력받고 호출하는 함수 만들기
# def func2(a, b):
#     print(a, b)

# func2(1, 2)

# # 값을 세개 입력받고 호출하는 함수 만들기
# def func3(a, b, c):
# #     print(a, b, c)

# # func3(1,2,3) 

# # # 매개변수의 개수가 달라져도
# # # 사용할 수 있는 함수 만들기

# # # 나머지 매개변수
# # # 나머지 매개변수를 만들때는 **별 두개
# dic = {'name':'둘리', 'age':10}
# print(dic.keys())
# print(dic.values())
# print(dic.items())

# def info(**kwargs):
#     # item 객체에서 요소를 꺼내면 tuple
#     # 구조 분해로 변수 두개에 key value 저장
#     for key, value in kwargs.items():
#         print(key, value)

# # # 함수 호출
# # func(a=1)
# # func(a=1, b=2)

# # # 나머지 매개변수를 사용하는 함수 만들기
# # # 사람의 정보를 입력받아 출력하는 함수 만들기
# # def info():
# #     pass

# info(name='둘리', age=10)
# info(name='도우너', age=8, address='서울')

# def calc(**kwargs):
#     for key, value in kwargs.items():
#         print(key)

# calc(apple=1200, banana=800, orange=1500)

# # 나머지 매개변수를 사용하여 입력받은 학생의 점수만 출력
# dic = {'철수':90, '영희':85, '민수':100}
# print(dic.values())
# print(dic.items())

# def show_scores(**kwargs):
#     for key, value in kwargs.items():
#         print(value)

# show_scores(철수=90, 영희=85, 민수=100)

# 나머지 매개변수를 사용하여 입력받은 도시 이름과 인구 수를 모두 출력
# (인구 수는 만명 단위)
# dic = {'seoul':950,'busan':340, 'incheon':300 }
# print(dic.values())
# print(dic.items())

# def show_population(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# show_population(seoul=950, busan=340, incheon=300)

# # 나머지 매개변수를 사용하여 입력받은 상품의 상품명만 출력

# dic = {'milk':2500, 'bread': 2000, 'egg':3000}
# print(dic.keys())

# def show_items(**kwargs):
#     for key in kwargs.keys():
#         print(key)
# show_items(milk=2500, bread=2000, egg=3000)

# 함수 만들기
# 두 수의 차를 구하는 함수 정의
# 매개변수: 함수에 필요한 입력값 숫자 두개
# 반환값: 두 수의 차를 구해서 결과를 반환
# 입력값 있고 반환값 있음
# 함수 내부에서 결과 화
# def sub(n1, n2):
#     return n1 - n2

# # 함수 호출
# result = sub(7, 3)
# print(result)

# # 인자를 순서와 상관없이 입력
# # 매개변수의 이름을 직접 지정
# result = sub(n2=3, n1=7)
# print(result)

# # 문자열 두개를 입력받아 연결하는 함수 정의
# def add_text(str1, str2):
#     print(f'{str1} {str2}')
# # 함수 호출
# add_text(str1='hello', str2='world')

# # 함수 만들기
# # 문자를 입력 받아 나쁜 말이 들어오면 종료하는 함수
# def say_nick(nick):
#     if nick == '바보':
#         return
#     print(f'나의 별명은 {nick}입니다')

# # 함수 호출
# say_nick('짱구')
# say_nick('바보')

# 함수 만들기
# def func():
#     a = 1
#     b = 2
#     c = 3
#     return a, b, c
# print(func())

# # 두 수를 입력 받아 
# 첫번째 수를 두번째 수로 나누고
# 몫을 출력하는 함수 만들기
# 나누는 수가 0이면
# '나누는 수는 0이 될 수 없습니다'를 출력하고
# 함수를 종료하세요
# 입력값을 검사하면
# 함수가 정상적으로 종료됨
# def divide(n1, n2):
#     if n2 == 0:
#         print('나누는 수는 0이 될 수 없습니다')
#         return    
#     print(n1 // n2)
# # 함수 호출
# divide(10, 2)
# divide(10, 0)


# 두 수를 더해서 합을 구하는 함수
# 식 자체는 성립되나
# 의도한대로 계산되지 않음
# 입력된 값이 숫자가 아니면, 더하기 계산을 할 필요가 없음
# 입력값이 숫자가 아니면 더하기를 수행 할 필요가 없으므로
# # 중간에 함수를 종료할 것
# def add(n1, n2):
#     # 식이 두개 이상이면 and 또는 or로 연결
#     # or: 둘 중 하나라면 참이면 참
#     if type(n1) != int or type(n2) != int:
#         print('입력받은 값이 숫자가 아닙니다')
#         return
    

#     print(f'{n1} + {n2} = {n1 + n2}')

# # 함수 호출
# add(3, 4)
# add(5, 'bb')
# add(10, 20)
# add('aa','bb')

# 나이를 입력받아 성인 여부를 출력하는 함수를 작성
# 20 -> 성인입니다
# 8 -> 성인이 아닙니다
# Q. 단 나이가 0보다 작으면 '잘못된 입력입니다'를 출력하고 함수 종료
# 입력값 검증하기
# 전달받은 값이 음수일 때는, 성인인지 아닌지 판단 할 필요가 없다
# def ag(age):
#     if age < 0:
#         print('잘못된 입력입니다')
#         return
#     if age >= 20: 
#         print('성인입니다')
#     else:        
#         print('성인이 아닙니다')  
# ag(20)
# ag(-5)

# 사람의 정보를 출력하는 함수 만들기
# 매개변수: 이름, 나이, 성별
# 성별의 초기값 설정. 기본값 f
# 초기값이 있는 매개변수는 항상 맨뒤에 배치해야함
# def info(name, age, gender='f'):
#     print(f'나의 이름은 {name}입니다')
#     print(f'나이는 {age}살 입니다')
#     if gender == 'm':
#         print('남자입니다')
#     else:
#         print('여자입니다')

# # 함수 호출
# # 도우너는 gender의 초기값을 사용해서 '남자'
# info('도우너', 8)
# # 둘리는 입력한 값 그대로 '여자'
# info('둘리', 10, 'f')


# 변수
# 두 a는 같은 변수가 아니다
# 전역변수와 지역변수를 나누는 이유:
# scope(유효범위)로 변수를 사용할 수 있는 범위를 확인하는 것
# a = 1 # 전역변수

# def func(a): # 지역변수 (함수 내부에서만 사용 가능)
#     a = a + 1

# func(a)
# print(a) # 1

# def func(b):
#     # b는 함수 내부에서 선언되어
#     # 함수가 끝나면 소멸됨
#     b = 3
#     print(b)
# # 함수 밖에서 b 사용하기
# print(b)

# 숫자 두개 입력받기
# input 함수로 받은 값은 str
# n1 = input('첫번쨰 숫자를 입력하세요: ')
# n2 = input('두번쨰 숫자를 입력하세요: ')

# # 두 수의 합 구하기
# # 먼저 형변환을 하고 더하기
# sum = int(n1) + int(n2)
# print('결과: ', sum)

# # 두 숫자를 입력받아 곱셈 결과를 출력
# n1 = input('첫번째 숫자: ')
# n2 = input('두번째 숫자: ')

# func = int(n1) * int(n2)
# print('결과: ', func)


# # 사용자로부터 이름과 나이를 입력받아 자기소개를 출력

# n1 = input('이름: ')
# n2 = input('나이: ')

# stri = str(n1) + str(n2)
# print(f'{n1}님의 나이는 {n2}세입니다')

# 사과 가격과 수량을 입력 받아 총 가격 계산

price = input()
cnt = input()
# 자료형 확인
print(type(price))

total = int(price) * int(cnt)
print('총 가격:', total)

# sum = int(n1) * int(n2)
#  print(sum,'원 입니다') 

