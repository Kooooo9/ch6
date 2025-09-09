# 파일 열기

# open(파일이름, 모드)
f = open('file1.txt', 'w')

for n in range(1, 11):
    # write 함수의 매개변수는 int
    # int -> str : 1 -> '1'
    f.write(f'{n}\n')

f.close()