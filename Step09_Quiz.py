# Step09_Quiz.py

'''
    비밀번호를 입력받아서 입력한 비밀번호가 8자 이상이면
    "사용가능한 비밀번호입니다"
    그렇지 않으면
    "사용 불가능한 비밀번호입니다"
'''


while True:
    input_password: str = input("비밀번호 입력 : ")    
    try:
        if len(input_password) >= 8:
            print("사용 가능한 비밀번호입니다.")
            break
        else:
            print("사용 불가능한 비밀번호입니다.")
            
    except Exception as e:
        print("오류가 발생했습니다. 다시 입력해주세요.")
        print("오류 내용 :", e)
        
        