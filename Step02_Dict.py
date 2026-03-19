## dict type 에 대해 알아보자

"""
    - dict type 은 key 와 value 의 쌍으로 이루어진 데이터 타입입니다.
    - key 는 고유한 값이어야 하며, value 는 어떤 데이터 타입이든 될 수 있습니다.
    - dict type 은 중괄호 {} 로 감싸서 표현하며, key 와 value 는 콜론 : 으로 구분됩니다.
    - dict type 은 순서가 없으며, 변경이 가능합니다.    
        
"""

# 회원 1명의 데이터
memInfo = {'num':1  , 'name' : 'youngsik', 'addr':  '용인' }

## dict type 의 key 는 고유한 값이어야 하며, value 는 어떤 데이터 타입이든 될 수 있습니다.
## 만약에 key 가 중복된다면, 마지막에 선언된 key 의 value 가 저장됩니다.


## print(memInfo['num']) -> memInfo.get('num') 으로 가져올 수 있습니다.

print(memInfo['num'])
print(memInfo['name'])
print(memInfo['addr'])



a = memInfo['num'] 
b = memInfo['name'] 
c = memInfo['addr'] 

print('수정 전 ',a)

memInfo['num'] = 2


print('수정 후 ',memInfo['num'])