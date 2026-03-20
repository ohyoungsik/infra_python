# Step09_if.py

'''
   임의이 숫자를 입력 받아서 입력한 수가 양수 이면 "양수입니다." 라고 출력하고, 음수이면 "음수입니다." 
   라고 출력을 해봐랏
   
'''

# while True:
#     input_msg = input("숫자를 입력하세요. : ")
    
#     try:
#         user_num = int(input_msg)  # 숫자로 변환 시도
        
#         if user_num > 0:
#             print("양수입니다.")
#         elif user_num < 0:
#             print("음수입니다.")

#         break  # 입력이 성공적으로 처리되면 루프 종료
#     except ValueError:
#         print("숫자를 입력해주세요.")

# 숫자를 입력 받는다.
input_num: int = int(input("임의의 정수 입력 : "))

if input_num > 0:
    print("입력한 숫자는 양수 입니다. ")
    
# 입력한 수가 짝수면 짝수 입니다. 홀수면 홀수 입니다. 라고 출력하기

if input_num % 2 == 0:
    print("입력한 숫자는 짝수 입니다. ")
else:
    print("입력한 숫자는 홀수 입니다. ")


print("종료 됩니다.")