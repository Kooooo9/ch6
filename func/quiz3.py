# 문자를 계속 입력 받다가 0이 들어오면 종료
# 반복문

# 반복문 for while
# for: list tuple range 등 데이터 개수만큼 -> 반복횟수가 명확
# while: 조건이 참인 동안 반복 -> 반복횟수가 모호

# 조건을 잘모르겠을 때 : 조건식을 True로 표현
while True:
    text = input('값을 입력하세요: ')
    # 입력받은 값이 0이면 종료(break)
    if text == '0':
        break

