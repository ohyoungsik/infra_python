# yaml 형식의 문자열 다루기

# yaml 문자열을 다룰 때는 외부 모듈을 pip 로 설치해서 import 해야한다.
# pip 는 python package manager 이다. python 에서 필요한 패키지를 설치할 때 사용하는 도구이다.

# pip를 사용하기 위해서는 가상 환경을 만들어야 한다. 가상 환경은 python 프로젝트마다 독립된 패키지와 라이브러리를 관리할 수 있게 해준다.
import yaml

info ='''
name : 영식
addr : 용인
foods :
 - 삼겹살
 - 김밥
company : 
  - name : 코리아IT아카데미
    addr : 강남  
  - name : 코리아IT아카데미2
    addr : 강남2
'''

## info에 들어 있는 문자열을 dict type 으로 바꾸자
# 그런 다음 dict 에 들어 있는 내용을 확인 후 다시 dict 에 있는 내용을 이용해서 yaml 형식의 문자열로 바꿔보자
# yaml 문자열을 dict type 으로 바꾸기
dictTypeData = yaml.safe_load(info)
# .load(info, Loader=yaml.FullLoader)
print(' yaml -> dictTypeData  :',dictTypeData)
print(' type check ------------------- ', type(dictTypeData))
# yaml 형식의 문자열로 바꾸기
yamlTypeData = yaml.dump(dictTypeData, allow_unicode=True)
print(' dict -> yamlTypeData  :', yamlTypeData)
print(' type check ------------------- ', type(yamlTypeData))




# # yaml 파일 읽기
# with open('yaml_test.yaml', 'r', encoding='utf-8') as file:
#     data = yaml.safe_load(file)

# # 파싱된 데이터 출력
# print(data)
# print(data['name'])
# print(data['foods'])