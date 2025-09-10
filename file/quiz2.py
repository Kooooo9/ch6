# # score.txt 파일을 읽고 합계와 평균을 구하세요
# f = open('score.txt', 'r')
# text = f.read()
# print(text)
# # 점수를 하나씩 꺼내기
# # list -> for str -> split
# # 문자열을 쪼개기 위한 구분자를 선택
# lis = text.split(' ')
# print(lis)
# # 총점 구하기
# sum = 0
# for n in lis:
#     sum = sum + int(n)
# print('총점:', sum)
# cnt = len(lis)
# print(cnt)
# print('평균:', sum/cnt)
# # print('총점:', sum)

# numbers.txt 파일을 읽고 짝수만 출력하세요

f = open('numbers.txt', 'r')

lis = f.readlines()

# 내용을 한줄씩 출력
for line in lis:
    # 짝수만 출력
    if int(line)%2 == 0: 
        print(line, end='')

f.close()
