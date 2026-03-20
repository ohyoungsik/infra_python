# Step13_jinja2.py

'''
    Template 문자열을 정의하고 어떤 데이터를 Template 문자열에 전달해서
    결과 문자열을 얻어내는 작업을 jinja2를 이용해서 테스트 해보자
    
    
    pip install jinja2
'''

from jinja2 import Template

# 테스트용 template 을 만든다.
my_template = """
    번호 : {{ num  }}
    이름 : {{ name }}
    주소 : {{ addr }}
    핸드폰 : {{ phonenumber }}
"""

# template 에 출력할 데이터를 준비
mem1 = {"num" : 1, "name" : "youngsik", "addr": "youngin"}
mem2 = {"num" : 2, "name" : "youngsik22", "addr": "youngin22"}

temp:Template = Template(my_template)
result1 = temp.render(mem1)
result2 = temp.render(mem2)

print('mem result 1 :  ', result1)
print('mem result 2 :  ', result2)
