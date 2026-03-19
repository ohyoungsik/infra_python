# Step04_Str2.py

"""
    여러분의 이름과 주소 좋아하는 음식 2가지를 작성해서 챗팅장에 올려보세요.
    
"""
# 이름과 주소 좋아하는 음식 2가지를 분리해서 변수에 담아서 활용하려면 어떻게하지?
import json


name = "영식"
addr = "용인"
foods = "삼겹살", "김밥"

# json 형식으로 해줘 (dict type)
# ysInfo = """{
#     "name" : "영식",
#     "addr" : "용인",
#     "foods" : ["삼겹살", "김밥"],
#     "company" :[
#         {
#         "name" : "코리아IT아카데미",
#         "addr" : "강남"
#         },
#         {
#         "name" : "코리아IT아카데미2",
#         "addr" : "강남2"
#         }
#     ]
# }
# """

ysInfo = """{
    "name" : "영식",
    "addr" : "용인",
    "foods" : ["삼겹살", "김밥"],
    "company" :[
        {
        "name" : "코리아IT아카데미",
        "addr" : "강남"
        },
        {
        "name" : "코리아IT아카데미2",
        "addr" : "강남2"
        }
    ]
}
"""
print('json 형식으로 작성한 정보 ', ysInfo)

#python에서 json 형식을 어떻게 활용해?

jsonInfo_dict = json.loads(ysInfo)
print('json 변환 ', jsonInfo_dict)

print('company 참조해볼게', jsonInfo_dict['company'][0]['name'])

resultInfo2 = json.dumps(jsonInfo_dict,indent=2, ensure_ascii=False)
print('json 변환2 ', resultInfo2)
