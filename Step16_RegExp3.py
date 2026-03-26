# Step16_RegExp3.py


# list 안에 어떤 서버의 로그가 들어있다고 가정
import re




logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]


# logs 에서  ERROR or WARN 로그만 찾아서 콘솔창에 출력해 보세요.


# [WARN] 또는 [ERROR] 로 문자열이 시작하는지 검증할 정규 표현식 만들기


# 첫글자가 W or A or R or N 인지를 검증할수 있는 정규 표현식
pattern1 = r"^[WARN]"
#  [WARN] 으로 시작하는지 검증할수 있는 정규 표현식
pattern2 = r"^\[WARN\]"
#  [ERROR] 으로 시작하는지 검증할수 있는 정규 표현식
pattern3 = r"^\[ERROR]\]"
# WARN or ERROR 로 시작하는지 검증할수 있는 정규 표현식
pattern4 = r"^(WARN|ERROR)"
# [WARN] or [ERROR] 로 시작하는지 검증할수 있는 정규 표현식
pattern = r"^\[(WARN|ERROR)\]"


for tmp in logs:
    # 정규표현식에 매칭되는 문자열이 있으면
    if re.search(pattern, tmp):
        print(tmp)
