# Step13_example.py

info:dict = {
    "num" : 1,
    "name" : 'yougsik',
    "body" : {
        "height" : 192,
        "weight" : 70,
    },
    "hobby" : ["피아노", "당구", "프로그래밍"] 
}

'''
    위의 info 안에 들어 있는 데이터를 이용해서 아래와 같은 형식의 문자열 출력
    
    번호 :1 
    이름 : youngsik
    키 : 192 cm
    몸무게 : 70
    취미 : 피아노, 당구, 프로그래밍
'''

from jinja2 import Template

info_Template = """
번호 : {{ num }}
이름 : {{ name }}
키 : {{ body.height }} cm
몸무게 : {{ body.weight }} kg
취미 :
{% for h in hobby %}
    - {{ h }}
{% endfor %}
"""

temp : Template = Template(info_Template)
result = temp.render(info)

print(result)