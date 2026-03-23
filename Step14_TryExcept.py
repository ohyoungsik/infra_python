# Step14_TryExcept.py

if __name__ == "__main__" :
  
  try:
      
    num1_str: str = input("젯수 입력 : ")
    num2_str: str = input("피젯수 입력 : ")
  
    num1: int = int(num1_str)
    num2: int = int(num2_str)
  
    result = num2/num1

    print(f"{num2}를 {num1} 으로 나눈 결과값 :  {result}")
  except ValueError as ve:  # ve에는 에러정보가 들어있음.
      print('valueError ve : ', ve)
      print("숫자 형식으로 입력해주세요.")
  except ZeroDivisionError as zde:
      print(' zde ' , zde )
      print('어떤 수를 0으로 나눌수는 없습니다.')
  
  print("중요한 마무리 작업을 합니다.")