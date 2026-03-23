# BinaryTest/gui02.py

# ui ToolKit 을 사용할수 있는 interface 객체 import 하기 
import tkinter as tk
from tkinter import messagebox

def clicked():
    print("버튼을 클릭했네요?")
    # Entry(입력창) 에 입력한 문자열 읽어오기
    input_value=entry.get().strip() # 좌우 공백 제거 strip()
    # 빈 값일 경우 안내 문구 표시
    
    try:
        if not input_value:
            result_label.config(text='값을 입력해주세요.')
        
            # 만일 입력한 수가 0 <= num <= 255 사이가 아니면 경고 알림 띄우기 
        if not set(input_value).issubset({"0", "1"}):
            messagebox.showerror("에러", "0 과 1만 입력해주세요.",fg='red')
            return
        
        if len(input_value) > 8:
            messagebox.showerror("에러", "8자리가 초과 되었습니다.",fg='red')
            return

            # 2진수를 10진수로 변경
        result_num = int(input_value,2)
            # 출력하기
        result_label.config(text=result_num, fg="blue")
    except Exception as e:
        result_label.config(text="숫자만 입력 가능 합니다", fg="red")
   

if __name__ == "__main__" :
    # root 창 생성
    root = tk.Tk()
    # 제목 설정 
    root.title("나의 App")
    # 창의 크기
    root.geometry("400x200")

    # 레이블
    label = tk.Label(root, text="2 진수를 10진수로 변환 (8자리 까지만 입력해주세요.)")
    # pady => padding y => y축 padding => 위아래 padding
    label.pack(pady=20)

    # 입력창 
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    entry.focus() # 포커스 주기

    # 버튼
    btn = tk.Button(root, text="변환", command=clicked, width=10, bg="lightgray")
    btn.pack(pady=15)

    # 결과 값을 출력할 Label
    result_label = tk.Label(root, text="결과...")
    result_label.pack(pady=20)

    # 창이 닫힐때 까지 무한 대기
    root.mainloop()
