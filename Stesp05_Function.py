# Step05_Function.py

"""
    function type
    
    function 이란?
    - 특정한 작업을 수행하는 코드의 집합
    - 반복적으로 사용되는 코드를 재사용하기 위해서 만들어진 코드의 묶음
    - function은 입력값을 받아서 특정한 작업을 수행한 후에 결과값을 반환할 수 있다.
    - function은 프로그램의 구조를 개선하고, 코드의 가독성을 높이며, 유지보수를 쉽게 해준다.
    - 함수는 저장된 code 를 다 실행하고 나면 원래 call 했던 위치로 실행의 흐름이 넘어온다.
    
    function의 구성 요소
    - function name : function의 이름, function을 호출할 때 사용된다.
    - parameters : function이 작업을 수행하는 데 필요한 입력값, function을 정의할 때 괄호 안에 작성된다.
    - function body : function이 수행하는 작업을 정의하는 코드 블록, function이 호출될 때 실행된다.
    - return value : function이 작업을 수행한 후에 반환하는 값, function body에서 return 키워드를 사용하여 지정된다.
    
"""

def test():
    print('test function')
    

def test2(arg): 
    print('test2 function with argument:', arg)
    print(f"전달 받은 내용: {arg}") ## f는 format string의 약자, 문자열 안에 {}로 감싸진 부분에 변수나 표현식의 값을 삽입할 수 있게 해준다.

test2("hello world")

def print_sum(a:int , b:int ) :
    result = a + b
    print(f"print_sum: {a} + {b} = {result}")
    
print_sum(5, 3)


def print_info(name: str, addr: str):
    print(f" 이름은 {name} 이고 주소는 {addr}")
    
print_info(name="영식", addr="용인시 수지구")

def get_sum(num1: int, num2: int) -> int:
    result = num1 + num2
    return result

result_get_sum = get_sum(5, 3)
print(f"get_sum: {result_get_sum}")


print('------------------- End of code -------------------')