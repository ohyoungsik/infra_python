# Step17_file3.py

import os


if __name__ == "__main__" :
  letter_path = os.path.join(os.getcwd(), "my_letter.txt")
  
  with open(letter_path, "r" , encoding="utf-8") as f:
      #문자열을 한줄씩 읽기
      print(f.readline())
      print(f.readline().strip()) # 좌우 공백이나 개행기호를 없애고 싶으면 .strip()까지 호출한다.
      print(f.readline())
      
  
  print('---------------------------------------------------------------------------')
      
  #반복문 처리 
  with open(letter_path,'r', encoding="utf-8") as f:
      for line in f:
          print(line.strip())
        
      
      # 파일 여러줄 읽기 ?
    #   print(f.readlines())
      
      