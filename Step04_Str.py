# str type 에 대해서 알아보자 ( 중요 ! )

# 양쪽에 공백이 포함되거나 포함될 가능성이 있는 문자열이 있다고 가정하자
# 만일 공백을 제거 하고 싶다면?
text = "   안녕하세요   "
# 양쪽 공백 제거
text_strip = text.strip()
# 왼쪽 공백 제거
text_lstrip = text.lstrip()
# 오른쪽 공백 제거
text_rstrip = text.rstrip()

print("원본 문자열:", text, "길이:", len(text))

myIp = '192.168.0.1'
# 문자열을 특정 구분자로 나누어서 리스트로 만들어주는 split() 함수를 이용해서 ip 주소를 . 으로 나눠보자
result2 = myIp.split('.')
print('result2 : ', result2)
result3 = ".".join(result2)
print('result3 : ', result3)
result4 = result3.replace('.','-')
print('result4 : ', result4)

result5 = "Hello! mimi".replace('mimi', 'youngsik')
print('result5 : ', result5)

upper_result5 = result5.upper()
print('upper ', upper_result5)
print('lower ', upper_result5.lower())

