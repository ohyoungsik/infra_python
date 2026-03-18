#list type 에 대해서 알아보기

nums = [10, 20, 30, 40, 50 ]
names =['kim', 'lee', 'park', 'choi', 'jung', 'oh']

# list 에 들어 있는 데이터를 앞에서 부터 순서대로 참조하면서 어떤 동작을 할 일들이 많이 발생한다.

for item in nums :
    print(item)
    
for name in names : 
    print(name)
    
r1 = range(10) # 0 ~ 9 까지의 숫자를 만들어내는 객체
print('r1 :  ',r1)
    
r2 = range(5) # 0 ~ 4 까지의 숫자를 만들어내는 객체
print('r2 :  ',r2)

for  i in range(len(names)) :
    print('r1 의 item : ',  i, names[i])
    

    