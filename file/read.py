# 반대로 파일의 내용을 읽어오기

# 읽기모드로 파일 열기
# # 파일이름, 모드(w,r)
# f = open('새파일.txt', 'r')

# # 파일의 내용 읽어오기
# # 읽기 함수들 중에서
# # readlines는 결과를 리스트로 반환
# # 결과는 리스트로 저장됨
# # 읽기 함수 중에서
# # read는 파일의 내용을
# # 문자열 하나로 반환
# text = f.read()


# # 문자열 안에 있는 알파벳을 하나씩 꺼내기
# # 함수의 인자: 구분자
# # split 함수는 공백을 기준으로
# # 문자열을 쪼개고 결과를 리스트로 반환
# # 함수의 형태
# # 함수의 사용법: 함수의 선언부 확인
# # 리턴값이 있을때:
# lis = text.split(' ')
# # 리턴값이 없을때:
# for ch in lis:
#     print(ch)
# # 사용이 끝났으면 닫기
# f.close()

# 반대로 파일 읽어오기
# 입력장치: 키보드 -> 파일

# 키보드에서 값 입력받기
# input()
# 파일에서 값 읽어오기
# f.read()
# 파일에서 내용 읽어오기

# 파일이름, 모드
# f = open('file1.txt', 'r')

# # read 함수로 내용 읽어오기
# # 결과를 리스트로 반환
# # 내용에는 줄바꿈이 포함됨 \n
# lis = f.readlines()

# # 한줄씩 출력하기
# for line in lis:
#     # end 매개변수 값 변경
#     print(line, end='')

# # print 함수에는 end라는 매개변수가 있고
# # 기본값이 \n
# print('1', end='\n')


# 파일 내용 읽어오기

# 파일이름, 모드
# 경로가 같을때는 파일 이름만 작성
# 파일에 한글이 있으면 인코딩 추가
# 새로운 내용 추가 : 11~21줄

#내용 추가 -> 쓰기 모드 (w 또는 a)
# 'w' 모드는 기존의 내용을 덮어씌움
# 'a' 모드는 이전 내용 뒤에 새로운 내용이 추가 됨
# f = open('file2.txt', 'a', encoding='utf-8')
# for i in range(11,21):
#     f.write(f'{i}번째 줄입니다\n')

# # read 함수로 내용 읽어오기
# # readlines는 리스트로 반환
# # lis = f.readlines()

# # # 내용을 한줄씩 출력
# #  for line in lis:
# #      print(line, end='')
# f.close()

# 파일을 쓰기 모드로 열기
f = open('new.txt', 'w')
f.write('hello world')
f.close()
# 위 코드를 간단하게 작성하기
# 위 코드와 같음
# with를 사용하면 마지막에 자동으로 close가 실행됨
with open('new.txt', 'w') as f:
    # 블록에는 수행하고 싶은 코드 작성
    f.write('hello world')