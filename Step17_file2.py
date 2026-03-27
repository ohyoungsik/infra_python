# Step17_file2.py

import os


if __name__ == "__main__" :

# 새로울 파일을 만들어서 문자열을 파일에 출력하기
    letter_path = os.path.join(os.getcwd(), "my_letter.txt")
    
    # "W"는 기존의 내용을 제거하고 덮어쓰기
    # append 모드가 2개일때 계속 추가가 된다.
    with open(letter_path,"w",encoding="utf=8") as f:
        f.write("To my Friend\n")
        f.write("Hello\n")
        f.write("Hello2\n")
        f.write("Hello3\n")
        
    #파일을 열어서 문자열 추가하기 append mode
    with open(letter_path,"a",encoding='utf-8') as f:
        f.write("KT 클라우드\n")
        f.write("KT 클라우드1\n")
        f.write("KT 클라우드2\n")
        
    print("my_letter.txt 파일이 생성 및 쓰기 완료")