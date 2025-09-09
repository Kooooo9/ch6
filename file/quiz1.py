# test.txt 파일을 만들고 다음과 같이 쓰세요

f = open('text.txt', 'w')
f.write('hello\n' 'hi')
f.close()

# score.txt 파일을 만들고 다음과 같이 쓰세요

f = open('score.txt', 'w')
f.write('80 90 70 100 60')
f.close()

# numbers.txt 파일을 만들고 다음과 같이 쓰세요
f = open('numbers.txt', 'w')

for n in range(10, 21):
    f.write(f'{n}\n')

f.close()