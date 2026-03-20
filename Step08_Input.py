# Step08_Input.py

# 콘솔창으로부터 문자열 입력 받기
# 주인장이 생각하는 숫자 
constNum = 10

# 입력 받은 문자열 출력하기

while True:
    input_msg = input("주인장이 생각한 숫자를 입력하세요. : ")
    
    try:
        user_num = int(input_msg)  # 숫자로 변환 시도
        if user_num == constNum:
            print("정답입니다.")
            break
        else:
            print("틀렸습니다.")
    except ValueError:
        print("숫자를 입력해주세요.")