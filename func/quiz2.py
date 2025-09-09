score = int(input('점수:'))

if score >= 60:
    print('합격')
else:
    print('불합격')

# 학생의 나이를 입력 받아 버스 요금을 계산하세요
age = int(input('나이:'))

if age <= 12:
    fare = 1000
elif age <= 18:
    fare = 1500
else:
    fare = 2000

print('버스 요금은', fare, '원 입니다.')

