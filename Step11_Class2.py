#Step11_Class2.py

class MyCar:
    
    ## __init__() : 생성자 (Constructor) 라고 불리는 특수한 메소드
    # 객체가 생성될 때 자동으로 호출되는 메소드로, 객체의 초기화 작업을 수행하는 역할을 한다.
    
    def __init__(self,name: str, speed: int):
        print('생성자가 호출됨')
        print('__init__ ----------- ',self)
        # 객체 고유의 저장소에 전달된 값을 저장한다.
        self.name=name     
        self.speed= speed
        
    def drive(self):
        print(f"{self.name}이(가) 시속 {self.speed} 로 부릉부릉~~") 


if __name__ == "__main__" :
  c1: MyCar = MyCar('소나타',100)
  c2: MyCar = MyCar('아반떼',500)
  c1.drive()
  c2.drive()
    