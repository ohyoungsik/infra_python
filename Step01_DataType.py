# 한줄 주석입니다.

"""

여러 줄 주석 테스트 ㅋㅋ

"""

print('Step01 시작')

# python 의 여러가지 데이터 type에 대해서 알아보자

# int type 
num1 = 10
age = 32

# float type
num2 = 10.1

# str type
myName = '영식'

ourName = """
이거는 어떻게 
출력이 될까 ?
"""


print(" 제 이름은 " + myName + " 입니다." + " 그리고 나이는 " , age , " 입니다")


print(ourName)


foods = ['삼겹살', '김밥', '닭발']

print(' 몇번 째 음식 인가 ',foods[2])

for food in foods:
    print (food)


memInfo = {'num':1  , 'name' : 'youngsik', 'addr':  '용인' }

print('뻘 건 점 찍기 전 ')


print(memInfo)

print (memInfo['num'])

print (' -function made-- ')

def store() :
    print('냉장고 문을 연다')
    print('물건을 저장한다.')
    print('냉장고 문을 닫는다')
    return True
    
print(store())

chatgpt = None


print('현재는 빈 값인가요 ? ',chatgpt)


isMan = True
isWoman = False
isDifferent = True
isRun= False

print('남자인가요 ? ',isMan)
print('여자인가요 ? ',isWoman)
print('다른가요 ? ',isDifferent)
print('달리는 중인가요 ? ',isRun)

print(type(isMan))
print(type(isWoman))
print(type(isDifferent))
print(type(isRun))
