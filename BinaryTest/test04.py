# test04.py

ip_addr =input("ip 주소입력 ex (192.168.0.7)  :   ")

ip_parts = ip_addr.split('.')

print(ip_parts)

binary_parts = []

for item in ip_parts:
    # :08b 는 뒤에서부터 읽으면 2(진수)로 변환하되 총 8자리로 변환하고 빈속은 0으로 채움
    print(f"{int(item):08b}")
    # 2진수 8자리로 구성된 값을 빈배열에 추가 (append)
    result = binary_parts.append(f"{int(item):08b}")
    
    
print('result2 ', binary_parts)

result3 = ".".join(binary_parts)
print('result3 ',result3) 