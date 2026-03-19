# Stop06_Tuple.py

"""
    tuple type
    
    tuple 이란?
    - 순서가 있다
    - 여러 type 의 데이터를 저장할 수 있다
    - 값 변경 불가능 (immutable)
    
    * list type 과 tuple type 의 차이점은 무엇일까?
    - list type 은 값 변경이 가능하지만 tuple type 은 값 변경이 불가능하다.
    - list type 은 대괄호 [] 로 감싸지만 tuple type 은 소괄호 () 로 감싼다.
    - list type 은 값 변경이 가능하기 때문에 append, remove, pop 등의 메소드를 사용할 수 있지만
      tuple type 은 값 변경이 불가능하기 때문에 이러한 메소드를 사용할 수 없다.
    
    1. list type 과 유사
    2. 읽기 전용  ( 수정, 삭제 불가)
    3. 기능이 적기 때문에 처리속도가 빠르다.
    
"""
tuple1: tuple = ("One", "Two", "Three")
tuple2: tuple = ("김구라", "해골", "원숭이")
tuple3: tuple = (10, "xxx", True)

tuple1.count("One") # tuple1 에서 "One" 이 몇개 있는지 세어준다.
tuple1.index("Two") # tuple1 에서 "Two" 가 몇번 인덱스에 있는지 알려준다.
# concat_tuple = tuple1.__add__(tuple3) # tuple1 과 tuple2 를 합쳐서 새로운 tuple 을 만들어준다.

concat_tuple = tuple1 + tuple3 # tuple1 과 tuple2 를 합쳐서 새로운 tuple 을 만들어준다.
print(' concat_tuple : ', concat_tuple)

# 두 변수에 있는 값을 서로 바꾸려면?
first = 'girls  generation'
second = 'black pink'
first, second = second, first
print(' first : ', first)
print(' second : ', second)

 
