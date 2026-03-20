# Step10_main.py

'''
    현재 파일 즉 Step10_main.py 파일이 메인으로 실행되는 파일인지 아니면
    다른 파일에서 import 되어 실행되는 파일인지를 구분하는 방법
    
    __name__ : 현재 파일이 메인으로 실행되는 파일이면 __main__ 이라는 문자열이 저장되고, 
    다른 파일에서 import 되어 실행되는 파일이면 현재 파일의 이름이 저장된다.
    
    다른 곳에서 import 했을 때 실행되지 않는 코드 블럭을 만들 때 사용한다.
    
    예시)
    1. python Step10_main.py  --> __name__ 에는 "__main__" 이 저장된다.
    2. from Step10_main import *  --> __name__ 에는 "Step10_main" 이 저장된다.
        
'''
print('Step10_main.py 파일이 실행됩니다.')
print('Step10_main.py ------ ',__name__)

 # 클래스 정의
class TestClass :
    pass

if __name__ == "__main__":
    print("현재 Step10_main.py 파일이 메인으로 실행되는 파일입니다.")
else:
    print("현재 파일이 다른 파일에서 import 되어 실행되는 파일입니다.")
    