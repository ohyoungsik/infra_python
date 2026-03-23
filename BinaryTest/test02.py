# Binary/test02.py

'''
    binary

'''


a = 0b1100
b = 0b1010

# a 와 b를 비트 AND 연산 (자리수 별로 모두가 1일 때 결과가 1이 된다.)
print('a & b', a & b)
print(' bin ', bin(a & b)) # 2진수 형식으로 변환

info = 0b1111_1111_1111_0000
print(info)
print(bin(info))

data1 = 0b1100_0011_1010_0001
data2 = 0b1100_0011_1010_0010
data3 = 0b1100_0011_1010_1011
data4 = 0b1100_0011_1010_1100

print(bin(info&data1))
print(bin(info&data2))
print(bin(info&data3))
print(bin(info&data4))