# Step14_TryExcept2.py

if __name__ == "__main__" :
  
  try:
      
    num1_str: str = input("젯수 입력 : ")
    num2_str: str = input("피젯수 입력 : ")
  
    num1: int = int(num1_str)
    num2: int = int(num2_str)
  
    result = num2/num1

    print(f"{num2}를 {num1} 으로 나눈 결과값 :  {result}")
  except Exception as e :
      print(' 어떤에러가 발생했습니다. ' , e)
  else: #예외가 발생하지 않으면 실행이 되는 블럭
      pass
  finally: #정상수행 or 예외가 발생해도 반드시 실행이 보장되는 블럭
      pass
      
  
  print("중요한 마무리 작업을 합니다.")