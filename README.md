# Python 기초 학습

## 📌 프로젝트 소개
이 저장소는 **Python 기초 문법과 기본 라이브러리 사용법**을 단계별로 정리한 학습용 예제 코드 모음입니다. 
- **언어**: Python 3.x
- **목적**: 자료형, 제어문, 컬렉션, 파일 입출력, YAML/JSON 처리 등을 실습
- **개발 기간**: 2026.03.19 ~

---

## 🚀 시작하기 (권장 작업 흐름)
### 1) 가상환경 생성 및 활성화 (Windows PowerShell)
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2) 필요한 패키지 설치
```powershell
pip install pyyaml
```

> 💡 나중에 requirements.txt를 만들어두면 `pip install -r requirements.txt`로 한 번에 설치 가능합니다.

---

## 🗂️ 파일/폴더 구성
| 파일 | 설명 |
|------|------|
| `Step01_DataType.py` | 기본 데이터 타입(숫자, 문자열, 불린 등) 예제 |
| `Step02_Dict.py` | 딕셔너리 사용법 예제 |
| `Step03_List.py`, `Step03_List2.py`, `Step03-1_List.py` | 리스트, 반복문, 리스트 컴프리헨션 등 |
| `Step04_Str.py`, `Step04_Str2.py`, `Step04_Str3.py` | 문자열 처리 + YAML/JSON 입출력 예제 |
| `yaml_test.yaml` | YAML 예제 데이터 |
| `json_test.json` | JSON 예제 데이터 |

---

## ▶️ 실행 방법
### 개별 파일 실행
```powershell
python Step04_Str3.py
```

### 원하는 단계부터 실행하기
- 예: `python Step02_Dict.py`, `python Step03_List.py` 등

---

## 💡 YAML/JSON 처리 예시
### YAML 파일 읽기 (`pyyaml` 사용)
```python
import yaml

with open('yaml_test.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

print(data)
```

### JSON 파일 읽기 (`json` 표준 라이브러리)
```python
import json

with open('json_test.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)
```

---

## ✅ 추가 팁
- 각 Step 파일 위에 주석으로 설명이 있으니 천천히 읽어보세요.
- 실습하면서 직접 코드를 수정하고 실행해보면 이해가 빠릅니다.

