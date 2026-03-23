# gui01.py
import tkinter as tk

if __name__ == "__main__" :
  def clicked():
    value = input_value.get().strip()
    if not value:
        result_label.config(text='값을 입력해주세요.')
        return
    try:
        dec = int(value)
    except ValueError:
        result_label.config(text='정수를 입력해주세요.')
        return

    if not (0 <= dec <= 255):
        result_label.config(text= "범위 초과 0에서 255 사이의 숫자만 입력해주세요.")
        return

    bin_value = (f"{dec:08b}")

    result_label.config(text=f"입력: {dec} -> 2진수: {bin_value}")


root = tk.Tk()

root.title('10 진수 -> 2진수 변환 프로그램')

# window size 
root.geometry('400x250')

label = tk.Label(root, text="안녕하세요.")
label.pack(pady=20)

# input
input_value = tk.Entry(root,font=('Arial',12))
input_value.pack(pady=5)
input_value.focus()

# button
btn = tk.Button(root,text="전송",command=clicked,width=10,bg="lightgray")
btn.pack(pady=15)


label2 = tk.Label(root, text="Result")
label2.pack(pady=5)

result_label = tk.Label(root, text="", fg='blue', font=('Arial', 8))
result_label.pack(pady=5)


root.mainloop()