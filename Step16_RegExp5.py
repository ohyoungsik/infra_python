# Step16_RegExp5.py

import re

if __name__ == "__main__" :
  input_id = input("아이디 입력 (영문자로 시작하고, 5~10 글자 이내, 특수문자 허용안함)")  
  
  pattern = r'^[a-zA-Z][a-zA-Z0-9_]{4,9}$' # 여기서 [a-zA-Z] 이게 한글자를 포함하기 때문에 {4,9} 이다 만약 없었다면 {5,9}
  # {4,} 최소값   -> 줄임 표현 + 
  # {,9} 최대값   -> 줄임 표현 *
  # {0,1} 0번 또는 1번 {1,0} 줄임 표현 -> ?

  if re.match(pattern, string=input_id):
    print("가입이 되었습니다.")
  else:
    print("사용할 수 없는 아이디 입니다.")