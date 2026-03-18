# Step03_Example.py

"""
    회원 한명의 정보는 번호, 이름, 주소로 이루어져 있다.
    그리고 그러한 회원이 어려명이다.
    여러명의 회원 목을을 하나의 묶음으로 (하나의 data) 로 순서대로 관리하고 싶다면...
    
"""

# 3명의 회원정보를 각각 dict type 으로 만들고 list에 담는 코드를 작성해보자

memList = [
    {'num':1  , 'name' : 'youngsik', 'addr':  '용인' },
    {'num':2  , 'name' : 'youngsik2', 'addr':  '서울' },
    {'num':3  , 'name' : 'youngsik3', 'addr':  '부산' }
]

for member in memList :
    print('회원 번호 : ', member['num'])
    print('회원 이름 : ', member['name'])
    print('회원 주소 : ', member['addr'])
    
    
a = memList
b = memList[0]
c = memList[0]['num']   
print('a : ', a)
print('b : ', b)        
print('c : ', c)



