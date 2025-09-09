# 파일을 쓰기 모드로 열기

# 한글 입력시 인코딩 설정 추가
f = open('file2.txt', 'w', encoding='utf_8')

# 1부터 10까지 출력하기
for i in range(1, 11):
    # i는 정수
    # int ->. str
    f.write(f'{i}번째 줄입니다\n')

f.close()