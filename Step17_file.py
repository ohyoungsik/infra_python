# Step17_file.py

import os


if __name__ == "__main__" :
  print(os.getcwd())  # cwd = current work directory
  
  # 파일 구분자 os.sep (window는 역슬레시, linux는 슬레시를 얻어낸다)
  print(os.sep)
  
  r'''
    현재 memo.txt 파일은 D:\playground\python_basic\memo.txt 의 경로에 존재한다.
    해당 경로를 문자열로 만들어보기
    
  '''
  
  # os.path.join() 을 이용하면 window 에서는 역슬레시로 조합하고 linux 에는 스래쉬로 조합
  path: str = os.path.join(os.getcwd(),"memo.txt")
  print(path)
  
  # with 구문을 이용해서 path 경로에 있는 text 파일을 읽기 (r) 전용으로 열어서 f 라는 별칭으로 사용한다.
  with open(path,"r",encoding="utf-8") as f:
      result = f.read()
      print(' memo.txt used')
      print(result)
  